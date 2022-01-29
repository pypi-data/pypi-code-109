import math
from typing import Dict

import torch
from torch.optim.optimizer import Optimizer

from pytorch_optimizer.gc import centralize_gradient
from pytorch_optimizer.types import BETAS, BUFFER, CLOSURE, DEFAULTS, LOSS, PARAMETERS


class Ranger(Optimizer):
    """
    Reference : https://github.com/lessw2020/Ranger-Deep-Learning-Optimizer
    Example :
        from pytorch_optimizer import Ranger
        ...
        model = YourModel()
        optimizer = Ranger(model.parameters())
        ...
        for input, output in data:
          optimizer.zero_grad()
          loss = loss_function(output, model(input))
          loss.backward()
          optimizer.step()
    """

    def __init__(
        self,
        params: PARAMETERS,
        lr: float = 1e-3,
        alpha: float = 0.5,
        k: int = 6,
        n_sma_threshold: int = 5,
        betas: BETAS = (0.95, 0.999),
        eps: float = 1e-5,
        weight_decay: float = 0.0,
        use_gc: bool = True,
        gc_conv_only: bool = False,
        adamd_debias_term: bool = False,
    ):
        """Ranger optimizer
        :param params: PARAMETERS. iterable of parameters to optimize or dicts defining parameter groups
        :param lr: float. learning rate
        :param betas: BETAS. coefficients used for computing running averages of gradient and the squared hessian trace
        :param weight_decay: float. weight decay (L2 penalty)
        :param n_sma_threshold: int. (recommended is 5)
        :param use_gc: bool. use Gradient Centralization (both convolution & fc layers)
        :param gc_conv_only: bool. use Gradient Centralization (only convolution layer)
        :param adamd_debias_term: bool. Only correct the denominator to avoid inflating step sizes early in training
        :param eps: float. term added to the denominator to improve numerical stability
        """
        self.lr = lr
        self.alpha = alpha
        self.k = k
        self.n_sma_threshold = n_sma_threshold
        self.betas = betas
        self.weight_decay = weight_decay
        self.use_gc = use_gc
        self.eps = eps

        self.gc_gradient_threshold: int = 3 if gc_conv_only else 1
        self.buffer: BUFFER = [[None, None, None] for _ in range(10)]

        self.check_valid_parameters()

        defaults: DEFAULTS = dict(
            lr=lr,
            alpha=alpha,
            k=k,
            step_counter=0,
            betas=betas,
            n_sma_threshold=n_sma_threshold,
            eps=eps,
            weight_decay=weight_decay,
            adamd_debias_term=adamd_debias_term,
        )
        super().__init__(params, defaults)

    def check_valid_parameters(self):
        if self.lr < 0.0:
            raise ValueError(f'Invalid learning rate : {self.lr}')
        if self.k < 1:
            raise ValueError(f'Invalid lookahead step {self.k}')
        if self.weight_decay < 0.0:
            raise ValueError(f'Invalid weight_decay : {self.weight_decay}')
        if not 0.0 <= self.betas[0] < 1.0:
            raise ValueError(f'Invalid beta_0 : {self.betas[0]}')
        if not 0.0 <= self.betas[1] < 1.0:
            raise ValueError(f'Invalid beta_1 : {self.betas[1]}')
        if self.eps < 0.0:
            raise ValueError(f'Invalid eps : {self.eps}')

    def __setstate__(self, state: Dict):
        super().__setstate__(state)

    def step(self, _: CLOSURE = None) -> LOSS:
        loss: LOSS = None

        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None:
                    continue

                grad = p.grad.data.float()
                if grad.is_sparse:
                    raise RuntimeError('Ranger optimizer does not support sparse gradients')

                p_data_fp32 = p.data.float()

                state = self.state[p]
                if len(state) == 0:
                    state['step'] = 0
                    state['exp_avg'] = torch.zeros_like(p_data_fp32)
                    state['exp_avg_sq'] = torch.zeros_like(p_data_fp32)
                    state['slow_buffer'] = torch.empty_like(p.data)
                    state['slow_buffer'].copy_(p.data)
                else:
                    state['exp_avg'] = state['exp_avg'].type_as(p_data_fp32)
                    state['exp_avg_sq'] = state['exp_avg_sq'].type_as(p_data_fp32)

                exp_avg, exp_avg_sq = state['exp_avg'], state['exp_avg_sq']
                beta1, beta2 = group['betas']

                if self.use_gc and grad.dim() > self.gc_gradient_threshold:
                    grad = centralize_gradient(grad, gc_conv_only=False)

                state['step'] += 1

                exp_avg.mul_(beta1).add_(grad, alpha=1 - beta1)
                exp_avg_sq.mul_(beta2).addcmul_(grad, grad, value=1 - beta2)

                bias_correction1 = 1 - beta1 ** state['step']

                buffered = self.buffer[int(state['step'] % 10)]

                if state['step'] == buffered[0]:
                    n_sma, step_size = buffered[1], buffered[2]
                else:
                    buffered[0] = state['step']
                    beta2_t = beta2 ** state['step']
                    n_sma_max = 2 / (1 - beta2) - 1
                    n_sma = n_sma_max - 2 * state['step'] * beta2_t / (1 - beta2_t)
                    buffered[1] = n_sma
                    if n_sma > self.n_sma_threshold:
                        rt = math.sqrt(
                            (1 - beta2_t)
                            * (n_sma - 4)
                            / (n_sma_max - 4)
                            * (n_sma - 2)
                            / n_sma
                            * n_sma_max
                            / (n_sma_max - 2)
                        )

                        if group['adamd_debias_term']:
                            step_size = rt
                        else:
                            step_size = rt / bias_correction1
                    else:
                        step_size = 1.0 / bias_correction1

                    buffered[2] = step_size

                if group['weight_decay'] != 0:
                    p_data_fp32.add_(p_data_fp32, alpha=-group['weight_decay'] * group['lr'])

                if n_sma > self.n_sma_threshold:
                    denom = exp_avg_sq.sqrt().add_(group['eps'])
                    p_data_fp32.addcdiv_(exp_avg, denom, value=-step_size * group['lr'])
                else:
                    p_data_fp32.add_(exp_avg, alpha=-step_size * group['lr'])

                p.data.copy_(p_data_fp32)

                if state['step'] % group['k'] == 0:
                    slow_p = state['slow_buffer']
                    slow_p.add_(p.data - slow_p, alpha=self.alpha)
                    p.data.copy_(slow_p)

        return loss
