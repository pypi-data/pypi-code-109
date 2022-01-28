import itertools
import os
from itertools import product
from typing import (
    Any,
    Hashable,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
)

import tlz as toolz

from .base import clone_key, get_name_from_key, tokenize
from .compatibility import prod
from .core import flatten, keys_in_tasks, reverse_dict
from .delayed import unpack_collections
from .highlevelgraph import HighLevelGraph, Layer
from .optimization import SubgraphCallable, fuse
from .utils import (
    _deprecated,
    apply,
    ensure_dict,
    homogeneous_deepmap,
    stringify,
    stringify_collection_keys,
)


class BlockwiseDep:
    """Blockwise-IO argument

    This is the base class for indexable Blockwise-IO arguments.
    When constructing a ``Blockwise`` Layer, one or more of the
    collection tuples passed in with ``indices`` may contain a
    ``BlockwiseDep`` instance (in place of a "real" collection name).
    This allows a new collection to be created (via IO) within a
    ``Blockwise`` layer.

    All ``BlockwiseDep`` instances must define a ``numblocks``
    attribute to speficy the number of blocks/partitions the
    object can support along each dimension. The object should
    also define a ``produces_tasks`` attribute to specify if
    any nested tasks will be passed to the Blockwise function.

    See Also
    --------
    dask.blockwise.Blockwise
    dask.blockwise.BlockwiseDepDict
    """

    numblocks: Tuple[int, ...]
    produces_tasks: bool

    def __getitem__(self, idx: Tuple[int, ...]) -> Any:
        """Return Blockwise-function arguments for a specific index"""
        raise NotImplementedError(
            "Must define `__getitem__` for `BlockwiseDep` subclass."
        )

    def get(self, idx: Tuple[int, ...], default) -> Any:
        """BlockwiseDep ``__getitem__`` Wrapper"""
        try:
            return self.__getitem__(idx)
        except KeyError:
            return default

    def __dask_distributed_pack__(
        self, required_indices: Optional[List[Tuple[int, ...]]] = None
    ):
        """Client-side serialization for ``BlockwiseDep`` objects.

        Should return a ``state`` dictionary, with msgpack-serializable
        values, that can be used to initialize a new ``BlockwiseDep`` object
        on a scheduler process.
        """
        raise NotImplementedError(
            "Must define `__dask_distributed_pack__` for `BlockwiseDep` subclass."
        )

    @classmethod
    def __dask_distributed_unpack__(cls, state):
        """Scheduler-side deserialization for ``BlockwiseDep`` objects.

        Should use an input ``state`` dictionary to initialize a new
        ``BlockwiseDep`` object.
        """
        raise NotImplementedError(
            "Must define `__dask_distributed_unpack__` for `BlockwiseDep` subclass."
        )

    def __repr__(self) -> str:
        return f"<{type(self).__name__} {self.numblocks}>"


class BlockwiseDepDict(BlockwiseDep):
    """Dictionary-based Blockwise-IO argument

    This is a dictionary-backed instance of ``BlockwiseDep``.
    The purpose of this class is to simplify the construction
    of IO-based Blockwise Layers with block/partition-dependent
    function arguments that are difficult to calculate at
    graph-materialization time.

    Examples
    --------

    Specify an IO-based function for the Blockwise Layer. Note
    that the function will be passed a single input object when
    the task is executed (e.g. a single ``tuple`` or ``dict``):

    >>> import pandas as pd
    >>> func = lambda x: pd.read_csv(**x)

    Use ``BlockwiseDepDict`` to define the input argument to
    ``func`` for each block/partition:

    >>> dep = BlockwiseDepDict(
    ...     mapping={
    ...         (0,) : {
    ...             "filepath_or_buffer": "data.csv",
    ...             "skiprows": 1,
    ...             "nrows": 2,
    ...             "names": ["a", "b"],
    ...         },
    ...         (1,) : {
    ...             "filepath_or_buffer": "data.csv",
    ...             "skiprows": 3,
    ...             "nrows": 2,
    ...             "names": ["a", "b"],
    ...         },
    ...     }
    ... )

    Construct a Blockwise Layer with ``dep`` speficied
    in the ``indices`` list:

    >>> layer = Blockwise(
    ...     output="collection-name",
    ...     output_indices="i",
    ...     dsk={"collection-name": (func, '_0')},
    ...     indices=[(dep, "i")],
    ...     numblocks={},
    ... )

    See Also
    --------
    dask.blockwise.Blockwise
    dask.blockwise.BlockwiseDep
    """

    def __init__(
        self,
        mapping: dict,
        numblocks: Optional[Tuple[int, ...]] = None,
        produces_tasks: bool = False,
    ):
        self.mapping = mapping
        self.produces_tasks = produces_tasks

        # By default, assume 1D shape
        self.numblocks = numblocks or (len(mapping),)

    def __getitem__(self, idx: Tuple[int, ...]) -> Any:
        return self.mapping[idx]

    def __dask_distributed_pack__(
        self, required_indices: Optional[List[Tuple[int, ...]]] = None
    ):
        from distributed.protocol import to_serialize

        if required_indices is None:
            required_indices = self.mapping.keys()

        return {
            "mapping": {k: to_serialize(self.mapping[k]) for k in required_indices},
            "numblocks": self.numblocks,
            "produces_tasks": self.produces_tasks,
        }

    @classmethod
    def __dask_distributed_unpack__(cls, state):
        return cls(**state)


def subs(task, substitution):
    """Create a new task with the values substituted

    This is like dask.core.subs, but takes a dict of many substitutions to
    perform simultaneously.  It is not as concerned with micro performance.
    """
    if isinstance(task, dict):
        return {k: subs(v, substitution) for k, v in task.items()}
    if type(task) in (tuple, list, set):
        return type(task)([subs(x, substitution) for x in task])
    try:
        return substitution[task]
    except (KeyError, TypeError):
        return task


def index_subs(ind, substitution):
    """A simple subs function that works both on tuples and strings"""
    if ind is None:
        return ind
    else:
        return tuple(substitution.get(c, c) for c in ind)


_BLOCKWISE_DEFAULT_PREFIX = "__dask_blockwise__"


def blockwise_token(i, prefix=_BLOCKWISE_DEFAULT_PREFIX):
    return prefix + "%d" % i


def blockwise(
    func,
    output,
    output_indices,
    *arrind_pairs,
    numblocks=None,
    concatenate=None,
    new_axes=None,
    dependencies=(),
    **kwargs,
):
    """Create a Blockwise symbolic mutable mapping

    This is like the ``make_blockwise_graph`` function, but rather than construct a
    dict, it returns a symbolic Blockwise object.

    ``*arrind_pairs`` is similar to those in `make_blockwise_graph`, but in addition to
    allowing for collections it can accept BlockwiseDep instances, which allows for lazy
    evaluation of arguments to ``func`` which might be different for different
    chunks/paritions.

    See Also
    --------
    make_blockwise_graph
    Blockwise
    """
    new_axes = new_axes or {}

    arrind_pairs = list(arrind_pairs)

    # Transform indices to canonical elements
    # We use terms like _0, and _1 rather than provided index elements
    unique_indices = {
        i for ii in arrind_pairs[1::2] if ii is not None for i in ii
    } | set(output_indices)
    sub = {k: blockwise_token(i, ".") for i, k in enumerate(sorted(unique_indices))}
    output_indices = index_subs(tuple(output_indices), sub)
    a_pairs_list = []
    for a in arrind_pairs[1::2]:
        if a is not None:
            val = tuple(a)
        else:
            val = a
        a_pairs_list.append(index_subs(val, sub))

    arrind_pairs[1::2] = a_pairs_list
    new_axes = {index_subs((k,), sub)[0]: v for k, v in new_axes.items()}

    # Unpack dask values in non-array arguments
    inputs = []
    inputs_indices = []
    for name, index in toolz.partition(2, arrind_pairs):
        inputs.append(name)
        inputs_indices.append(index)

    # Unpack delayed objects in kwargs
    new_keys = {n for c in dependencies for n in c.__dask_layers__()}
    if kwargs:
        # replace keys in kwargs with _0 tokens
        new_tokens = tuple(
            blockwise_token(i) for i in range(len(inputs), len(inputs) + len(new_keys))
        )
        sub = dict(zip(new_keys, new_tokens))
        inputs.extend(new_keys)
        inputs_indices.extend((None,) * len(new_keys))
        kwargs = subs(kwargs, sub)

    indices = [(k, v) for k, v in zip(inputs, inputs_indices)]
    keys = map(blockwise_token, range(len(inputs)))

    # Construct local graph
    if not kwargs:
        subgraph = {output: (func,) + tuple(keys)}
    else:
        _keys = list(keys)
        if new_keys:
            _keys = _keys[: -len(new_keys)]
        kwargs2 = (dict, list(map(list, kwargs.items())))
        subgraph = {output: (apply, func, _keys, kwargs2)}

    # Construct final output
    subgraph = Blockwise(
        output,
        output_indices,
        subgraph,
        indices,
        numblocks=numblocks,
        concatenate=concatenate,
        new_axes=new_axes,
    )
    return subgraph


class Blockwise(Layer):
    """Tensor Operation

    This is a lazily constructed mapping for tensor operation graphs.
    This defines a dictionary using an operation and an indexing pattern.
    It is built for many operations like elementwise, transpose, tensordot, and
    so on.  We choose to keep these as symbolic mappings rather than raw
    dictionaries because we are able to fuse them during optimization,
    sometimes resulting in much lower overhead.

    Parameters
    ----------
    output: str
        The name of the output collection.  Used in keynames
    output_indices: tuple
        The output indices, like ``('i', 'j', 'k')`` used to determine the
        structure of the block computations
    dsk: dict
        A small graph to apply per-output-block.  May include keys from the
        input indices.
    indices: Tuple[Tuple[str, Optional[Tuple[str, ...]]], ...]
        An ordered mapping from input key name, like ``'x'``
        to input indices, like ``('i', 'j')``
        Or includes literals, which have ``None`` for an index value.
        In place of input-key names, the first tuple element may also be a
        ``BlockwiseDep`` object.
    numblocks: Mapping[key, Sequence[int]]
        Number of blocks along each dimension for each input
    concatenate: bool
        Whether or not to pass contracted dimensions as a list of inputs or a
        single input to the block function
    new_axes: Mapping
        New index dimensions that may have been created and their size,
        e.g. ``{'j': 2, 'k': 3}``
    output_blocks: Set[Tuple[int, ...]]
        Specify a specific set of required output blocks. Since the graph
        will only contain the necessary tasks to generate these outputs,
        this kwarg can be used to "cull" the abstract layer (without needing
        to materialize the low-level graph).
    annotations: dict (optional)
        Layer annotations
    io_deps: Dict[str, BlockwiseDep] (optional)
        Dictionary containing the mapping between "place-holder" collection
        keys and ``BlockwiseDep``-based objects.
        **WARNING**: This argument should only be used internally (for culling,
        fusion and cloning of existing Blockwise layers). Explicit use of this
        argument will be deprecated in the future.

    See Also
    --------
    dask.blockwise.blockwise
    dask.array.blockwise
    """

    output: str
    output_indices: Tuple[str, ...]
    dsk: Mapping[str, tuple]
    indices: Tuple[Tuple[str, Optional[Tuple[str, ...]]], ...]
    numblocks: Mapping[str, Sequence[int]]
    concatenate: Optional[bool]
    new_axes: Mapping[str, int]
    output_blocks: Optional[Set[Tuple[int, ...]]]

    def __init__(
        self,
        output: str,
        output_indices: Iterable[str],
        dsk: Mapping[str, tuple],
        indices: Iterable[Tuple[Union[str, BlockwiseDep], Optional[Iterable[str]]]],
        numblocks: Mapping[str, Sequence[int]],
        concatenate: bool = None,
        new_axes: Mapping[str, int] = None,
        output_blocks: Set[Tuple[int, ...]] = None,
        annotations: Mapping[str, Any] = None,
        io_deps: Optional[Mapping[str, BlockwiseDep]] = None,
    ):
        super().__init__(annotations=annotations)
        self.output = output
        self.output_indices = tuple(output_indices)
        self.output_blocks = output_blocks
        self.dsk = dsk

        # Remove `BlockwiseDep` arguments from input indices
        # and add them to `self.io_deps`.
        # TODO: Remove `io_deps` and handle indexable objects
        # in `self.indices` throughout `Blockwise`.
        self.indices = []
        self.numblocks = numblocks
        self.io_deps = io_deps or {}
        for dep, ind in indices:
            name = dep
            if isinstance(dep, BlockwiseDep):
                name = tokenize(dep)
                self.io_deps[name] = dep
                self.numblocks[name] = dep.numblocks
            self.indices.append((name, tuple(ind) if ind is not None else ind))
        self.indices = tuple(self.indices)

        # optimize_blockwise won't merge where `concatenate` doesn't match, so
        # enforce a canonical value if there are no axes for reduction.
        output_indices_set = set(self.output_indices)
        if concatenate is not None and all(
            i in output_indices_set
            for name, ind in self.indices
            if ind is not None
            for i in ind
        ):
            concatenate = None
        self.concatenate = concatenate
        self.new_axes = new_axes or {}

    @property
    def dims(self):
        """Returns a dictionary mapping between each index specified in
        `self.indices` and the number of output blocks for that indice.
        """
        if not hasattr(self, "_dims"):
            self._dims = _make_dims(self.indices, self.numblocks, self.new_axes)
        return self._dims

    def __repr__(self):
        return f"Blockwise<{self.indices} -> {self.output}>"

    @property
    def _dict(self):
        if hasattr(self, "_cached_dict"):
            return self._cached_dict["dsk"]
        else:
            keys = tuple(map(blockwise_token, range(len(self.indices))))
            dsk, _ = fuse(self.dsk, [self.output])
            func = SubgraphCallable(dsk, self.output, keys)

            dsk = make_blockwise_graph(
                func,
                self.output,
                self.output_indices,
                *list(toolz.concat(self.indices)),
                new_axes=self.new_axes,
                numblocks=self.numblocks,
                concatenate=self.concatenate,
                output_blocks=self.output_blocks,
                dims=self.dims,
                io_deps=self.io_deps,
            )

            self._cached_dict = {"dsk": dsk}
        return self._cached_dict["dsk"]

    def get_output_keys(self):
        if self.output_blocks:
            # Culling has already generated a list of output blocks
            return {(self.output, *p) for p in self.output_blocks}

        # Return all possible output keys (no culling)
        return {
            (self.output, *p)
            for p in itertools.product(
                *[range(self.dims[i]) for i in self.output_indices]
            )
        }

    def __getitem__(self, key):
        return self._dict[key]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self) -> int:
        # same method as `get_output_keys`, without manifesting the keys themselves
        return (
            len(self.output_blocks)
            if self.output_blocks
            else prod(self.dims[i] for i in self.output_indices)
        )

    def is_materialized(self):
        return hasattr(self, "_cached_dict")

    def __dask_distributed_pack__(
        self, all_hlg_keys, known_key_dependencies, client, client_keys
    ):
        from distributed.protocol import to_serialize
        from distributed.utils import CancelledError
        from distributed.utils_comm import unpack_remotedata
        from distributed.worker import dumps_function

        keys = tuple(map(blockwise_token, range(len(self.indices))))
        dsk, _ = fuse(self.dsk, [self.output])

        # Embed literals in `dsk`
        keys2 = []
        indices2 = []
        global_dependencies = set()
        for key, (val, index) in zip(keys, self.indices):
            if index is None:
                try:
                    val_is_a_key = val in all_hlg_keys
                except TypeError:  # not hashable
                    val_is_a_key = False
                if val_is_a_key:
                    keys2.append(key)
                    indices2.append((val, index))
                    global_dependencies.add(stringify(val))
                else:
                    dsk[key] = val  # Literal
            else:
                keys2.append(key)
                indices2.append((val, index))

        dsk = (SubgraphCallable(dsk, self.output, tuple(keys2)),)
        dsk, dsk_unpacked_futures = unpack_remotedata(dsk, byte_keys=True)

        # Handle `io_deps` serialization. Assume each element
        # is a `BlockwiseDep`-based object.
        packed_io_deps = {}
        inline_tasks = False
        for name, blockwise_dep in self.io_deps.items():
            packed_io_deps[name] = {
                "__module__": blockwise_dep.__module__,
                "__name__": type(blockwise_dep).__name__,
                # TODO: Pass a `required_indices` list to __pack__
                "state": blockwise_dep.__dask_distributed_pack__(),
            }
            inline_tasks = inline_tasks or blockwise_dep.produces_tasks

        # Dump (pickle + cache) the function here if we know `make_blockwise_graph`
        # will NOT be producing "nested" tasks (via `__dask_distributed_unpack__`).
        #
        # If `make_blockwise_graph` DOES need to produce nested tasks later on, it
        # will need to call `to_serialize` on the entire task.  That will be a
        # problem if the function was already pickled here. Therefore, we want to
        # call `to_serialize` on the function if we know there will be nested tasks.
        #
        # We know there will be nested tasks if either:
        #   (1) `concatenate=True`   # Check `self.concatenate`
        #   (2) `inline_tasks=True`  # Check `BlockwiseDep.produces_tasks`
        #
        # We do not call `to_serialize` in ALL cases, because that code path does
        # not cache the function on the scheduler or worker (or warn if there are
        # large objects being passed into the graph).  However, in the future,
        # single-pass serialization improvements should allow us to remove this
        # special logic altogether.
        func = (
            to_serialize(dsk[0])
            if (self.concatenate or inline_tasks)
            else dumps_function(dsk[0])
        )
        func_future_args = dsk[1:]

        indices = list(toolz.concat(indices2))
        indices, indices_unpacked_futures = unpack_remotedata(indices, byte_keys=True)

        # Check the legality of the unpacked futures
        for future in itertools.chain(dsk_unpacked_futures, indices_unpacked_futures):
            if future.client is not client:
                raise ValueError(
                    "Inputs contain futures that were created by another client."
                )
            if stringify(future.key) not in client.futures:
                raise CancelledError(stringify(future.key))

        # All blockwise tasks will depend on the futures in `indices`
        global_dependencies |= {stringify(f.key) for f in indices_unpacked_futures}

        return {
            "output": self.output,
            "output_indices": self.output_indices,
            "func": func,
            "func_future_args": func_future_args,
            "global_dependencies": global_dependencies,
            "indices": indices,
            "is_list": [isinstance(x, list) for x in indices],
            "numblocks": self.numblocks,
            "concatenate": self.concatenate,
            "new_axes": self.new_axes,
            "output_blocks": self.output_blocks,
            "dims": self.dims,
            "io_deps": packed_io_deps,
        }

    @classmethod
    def __dask_distributed_unpack__(cls, state, dsk, dependencies):
        from distributed.protocol.serialize import import_allowed_module

        # Make sure we convert list items back from tuples in `indices`.
        # The msgpack serialization will have converted lists into
        # tuples, and tuples may be stringified during graph
        # materialization (bad if the item was not a key).
        indices = [
            list(ind) if is_list else ind
            for ind, is_list in zip(state["indices"], state["is_list"])
        ]

        # Unpack io_deps state
        io_deps = {}
        for replace_name, packed_dep in state["io_deps"].items():
            mod = import_allowed_module(packed_dep["__module__"])
            dep_cls = getattr(mod, packed_dep["__name__"])
            io_deps[replace_name] = dep_cls.__dask_distributed_unpack__(
                packed_dep["state"]
            )

        layer_dsk, layer_deps = make_blockwise_graph(
            state["func"],
            state["output"],
            state["output_indices"],
            *indices,
            new_axes=state["new_axes"],
            numblocks=state["numblocks"],
            concatenate=state["concatenate"],
            output_blocks=state["output_blocks"],
            dims=state["dims"],
            return_key_deps=True,
            deserializing=True,
            func_future_args=state["func_future_args"],
            io_deps=io_deps,
        )
        g_deps = state["global_dependencies"]

        # Stringify layer graph and dependencies
        layer_dsk = {
            stringify(k): stringify_collection_keys(v) for k, v in layer_dsk.items()
        }
        deps = {
            stringify(k): {stringify(d) for d in v} | g_deps
            for k, v in layer_deps.items()
        }
        return {"dsk": layer_dsk, "deps": deps}

    def _cull_dependencies(self, all_hlg_keys, output_blocks):
        """Determine the necessary dependencies to produce `output_blocks`.

        This method does not require graph materialization.
        """

        # Check `concatenate` option
        concatenate = None
        if self.concatenate is True:
            from dask.array.core import concatenate_axes as concatenate

        # Generate coordinate map
        (coord_maps, concat_axes, dummies) = _get_coord_mapping(
            self.dims,
            self.output,
            self.output_indices,
            self.numblocks,
            self.indices,
            concatenate,
        )

        # Gather constant dependencies (for all output keys)
        const_deps = set()
        for (arg, ind) in self.indices:
            if ind is None:
                try:
                    if arg in all_hlg_keys:
                        const_deps.add(arg)
                except TypeError:
                    pass  # unhashable

        # Get dependencies for each output block
        key_deps = {}
        for out_coords in output_blocks:
            deps = set()
            coords = out_coords + dummies
            for cmap, axes, (arg, ind) in zip(coord_maps, concat_axes, self.indices):
                if ind is not None and arg not in self.io_deps:
                    arg_coords = tuple(coords[c] for c in cmap)
                    if axes:
                        tups = lol_product((arg,), arg_coords)
                        deps.update(flatten(tups))
                        if concatenate:
                            tups = (concatenate, tups, axes)
                    else:
                        tups = (arg,) + arg_coords
                        deps.add(tups)
            key_deps[(self.output,) + out_coords] = deps | const_deps

        return key_deps

    def _cull(self, output_blocks):
        return Blockwise(
            self.output,
            self.output_indices,
            self.dsk,
            self.indices,
            self.numblocks,
            concatenate=self.concatenate,
            new_axes=self.new_axes,
            output_blocks=output_blocks,
            annotations=self.annotations,
            io_deps=self.io_deps,
        )

    def cull(
        self, keys: set, all_hlg_keys: Iterable
    ) -> Tuple[Layer, Mapping[Hashable, set]]:
        # Culling is simple for Blockwise layers.  We can just
        # collect a set of required output blocks (tuples), and
        # only construct graph for these blocks in `make_blockwise_graph`

        output_blocks = set()
        for key in keys:
            if key[0] == self.output:
                output_blocks.add(key[1:])
        culled_deps = self._cull_dependencies(all_hlg_keys, output_blocks)
        out_size_iter = (self.dims[i] for i in self.output_indices)
        if prod(out_size_iter) != len(culled_deps):
            culled_layer = self._cull(output_blocks)
            return culled_layer, culled_deps
        else:
            return self, culled_deps

    def clone(
        self,
        keys: set,
        seed: Hashable,
        bind_to: Hashable = None,
    ) -> Tuple[Layer, bool]:
        names = {get_name_from_key(k) for k in keys}
        # We assume that 'keys' will contain either all or none of the output keys of
        # each of the layers, because clone/bind are always invoked at collection level.
        # Asserting this is very expensive, so we only check it during unit tests.
        if "PYTEST_CURRENT_TEST" in os.environ:
            assert not self.get_output_keys() - keys
            for name, nb in self.numblocks.items():
                if name in names:
                    for block in product(*(list(range(nbi)) for nbi in nb)):
                        assert (name, *block) in keys

        is_leaf = True

        indices = []
        for k, idxv in self.indices:
            if k in names:
                is_leaf = False
                k = clone_key(k, seed)
            indices.append((k, idxv))

        numblocks = {}
        for k, nbv in self.numblocks.items():
            if k in names:
                is_leaf = False
                k = clone_key(k, seed)
            numblocks[k] = nbv

        dsk = {clone_key(k, seed): v for k, v in self.dsk.items()}

        if bind_to is not None and is_leaf:
            from .graph_manipulation import chunks

            # It's always a Delayed generated by dask.graph_manipulation.checkpoint;
            # the layer name always matches the key
            assert isinstance(bind_to, str)
            dsk = {k: (chunks.bind, v, f"_{len(indices)}") for k, v in dsk.items()}
            indices.append((bind_to, None))

        return (
            Blockwise(
                output=clone_key(self.output, seed),
                output_indices=self.output_indices,
                dsk=dsk,
                indices=indices,
                numblocks=numblocks,
                concatenate=self.concatenate,
                new_axes=self.new_axes,
                output_blocks=self.output_blocks,
                annotations=self.annotations,
                io_deps=self.io_deps,
            ),
            (bind_to is not None and is_leaf),
        )


def _get_coord_mapping(
    dims,
    output,
    out_indices,
    numblocks,
    argpairs,
    concatenate,
):
    """Calculate coordinate mapping for graph construction.

    This function handles the high-level logic behind Blockwise graph
    construction. The output is a tuple containing: The mapping between
    input and output block coordinates (`coord_maps`), the axes along
    which to concatenate for each input (`concat_axes`), and the dummy
    indices needed for broadcasting (`dummies`).

    Used by `make_blockwise_graph` and `Blockwise._cull_dependencies`.

    Parameters
    ----------
    dims : dict
        Mapping between each index specified in `argpairs` and
        the number of output blocks for that index. Corresponds
        to the Blockwise `dims` attribute.
    output : str
        Corresponds to the Blockwise `output` attribute.
    out_indices : tuple
        Corresponds to the Blockwise `output_indices` attribute.
    numblocks : dict
        Corresponds to the Blockwise `numblocks` attribute.
    argpairs : tuple
        Corresponds to the Blockwise `indices` attribute.
    concatenate : bool
        Corresponds to the Blockwise `concatenate` attribute.
    """

    block_names = set()
    all_indices = set()
    for name, ind in argpairs:
        if ind is not None:
            block_names.add(name)
            for x in ind:
                all_indices.add(x)
    assert set(numblocks) == block_names

    dummy_indices = all_indices - set(out_indices)

    # For each position in the output space, we'll construct a
    # "coordinate set" that consists of
    # - the output indices
    # - the dummy indices
    # - the dummy indices, with indices replaced by zeros (for broadcasting), we
    #   are careful to only emit a single dummy zero when concatenate=True to not
    #   concatenate the same array with itself several times.
    # - a 0 to assist with broadcasting.

    index_pos, zero_pos = {}, {}
    for i, ind in enumerate(out_indices):
        index_pos[ind] = i
        zero_pos[ind] = -1

    _dummies_list = []
    for i, ind in enumerate(dummy_indices):
        index_pos[ind] = 2 * i + len(out_indices)
        zero_pos[ind] = 2 * i + 1 + len(out_indices)
        reps = 1 if concatenate else dims[ind]
        _dummies_list.append([list(range(dims[ind])), [0] * reps])

    # ([0, 1, 2], [0, 0, 0], ...)  For a dummy index of dimension 3
    dummies = tuple(itertools.chain.from_iterable(_dummies_list))
    dummies += (0,)

    # For each coordinate position in each input, gives the position in
    # the coordinate set.
    coord_maps = []

    # Axes along which to concatenate, for each input
    concat_axes = []
    for arg, ind in argpairs:
        if ind is not None:
            coord_maps.append(
                [
                    zero_pos[i] if nb == 1 else index_pos[i]
                    for i, nb in zip(ind, numblocks[arg])
                ]
            )
            concat_axes.append([n for n, i in enumerate(ind) if i in dummy_indices])
        else:
            coord_maps.append(None)
            concat_axes.append(None)

    return coord_maps, concat_axes, dummies


def make_blockwise_graph(
    func,
    output,
    out_indices,
    *arrind_pairs,
    numblocks=None,
    concatenate=None,
    new_axes=None,
    output_blocks=None,
    dims=None,
    deserializing=False,
    func_future_args=None,
    return_key_deps=False,
    io_deps=None,
    **kwargs,
):
    """Tensor operation

    Applies a function, ``func``, across blocks from many different input
    collections.  We arrange the pattern with which those blocks interact with
    sets of matching indices.  E.g.::

        make_blockwise_graph(func, 'z', 'i', 'x', 'i', 'y', 'i')

    yield an embarrassingly parallel communication pattern and is read as

        $$ z_i = func(x_i, y_i) $$

    More complex patterns may emerge, including multiple indices::

        make_blockwise_graph(func, 'z', 'ij', 'x', 'ij', 'y', 'ji')

        $$ z_{ij} = func(x_{ij}, y_{ji}) $$

    Indices missing in the output but present in the inputs results in many
    inputs being sent to one function (see examples).

    Examples
    --------
    Simple embarrassing map operation

    >>> inc = lambda x: x + 1
    >>> make_blockwise_graph(inc, 'z', 'ij', 'x', 'ij', numblocks={'x': (2, 2)})  # doctest: +SKIP
    {('z', 0, 0): (inc, ('x', 0, 0)),
     ('z', 0, 1): (inc, ('x', 0, 1)),
     ('z', 1, 0): (inc, ('x', 1, 0)),
     ('z', 1, 1): (inc, ('x', 1, 1))}

    Simple operation on two datasets

    >>> add = lambda x, y: x + y
    >>> make_blockwise_graph(add, 'z', 'ij', 'x', 'ij', 'y', 'ij', numblocks={'x': (2, 2),
    ...                                                      'y': (2, 2)})  # doctest: +SKIP
    {('z', 0, 0): (add, ('x', 0, 0), ('y', 0, 0)),
     ('z', 0, 1): (add, ('x', 0, 1), ('y', 0, 1)),
     ('z', 1, 0): (add, ('x', 1, 0), ('y', 1, 0)),
     ('z', 1, 1): (add, ('x', 1, 1), ('y', 1, 1))}

    Operation that flips one of the datasets

    >>> addT = lambda x, y: x + y.T  # Transpose each chunk
    >>> #                                        z_ij ~ x_ij y_ji
    >>> #               ..         ..         .. notice swap
    >>> make_blockwise_graph(addT, 'z', 'ij', 'x', 'ij', 'y', 'ji', numblocks={'x': (2, 2),
    ...                                                       'y': (2, 2)})  # doctest: +SKIP
    {('z', 0, 0): (add, ('x', 0, 0), ('y', 0, 0)),
     ('z', 0, 1): (add, ('x', 0, 1), ('y', 1, 0)),
     ('z', 1, 0): (add, ('x', 1, 0), ('y', 0, 1)),
     ('z', 1, 1): (add, ('x', 1, 1), ('y', 1, 1))}

    Dot product with contraction over ``j`` index.  Yields list arguments

    >>> make_blockwise_graph(dotmany, 'z', 'ik', 'x', 'ij', 'y', 'jk', numblocks={'x': (2, 2),
    ...                                                          'y': (2, 2)})  # doctest: +SKIP
    {('z', 0, 0): (dotmany, [('x', 0, 0), ('x', 0, 1)],
                            [('y', 0, 0), ('y', 1, 0)]),
     ('z', 0, 1): (dotmany, [('x', 0, 0), ('x', 0, 1)],
                            [('y', 0, 1), ('y', 1, 1)]),
     ('z', 1, 0): (dotmany, [('x', 1, 0), ('x', 1, 1)],
                            [('y', 0, 0), ('y', 1, 0)]),
     ('z', 1, 1): (dotmany, [('x', 1, 0), ('x', 1, 1)],
                            [('y', 0, 1), ('y', 1, 1)])}

    Pass ``concatenate=True`` to concatenate arrays ahead of time

    >>> make_blockwise_graph(f, 'z', 'i', 'x', 'ij', 'y', 'ij', concatenate=True,
    ...     numblocks={'x': (2, 2), 'y': (2, 2,)})  # doctest: +SKIP
    {('z', 0): (f, (concatenate_axes, [('x', 0, 0), ('x', 0, 1)], (1,)),
                   (concatenate_axes, [('y', 0, 0), ('y', 0, 1)], (1,)))
     ('z', 1): (f, (concatenate_axes, [('x', 1, 0), ('x', 1, 1)], (1,)),
                   (concatenate_axes, [('y', 1, 0), ('y', 1, 1)], (1,)))}

    Supports Broadcasting rules

    >>> make_blockwise_graph(add, 'z', 'ij', 'x', 'ij', 'y', 'ij', numblocks={'x': (1, 2),
    ...                                                      'y': (2, 2)})  # doctest: +SKIP
    {('z', 0, 0): (add, ('x', 0, 0), ('y', 0, 0)),
     ('z', 0, 1): (add, ('x', 0, 1), ('y', 0, 1)),
     ('z', 1, 0): (add, ('x', 0, 0), ('y', 1, 0)),
     ('z', 1, 1): (add, ('x', 0, 1), ('y', 1, 1))}

    Support keyword arguments with apply

    >>> def f(a, b=0): return a + b
    >>> make_blockwise_graph(f, 'z', 'i', 'x', 'i', numblocks={'x': (2,)}, b=10)  # doctest: +SKIP
    {('z', 0): (apply, f, [('x', 0)], {'b': 10}),
     ('z', 1): (apply, f, [('x', 1)], {'b': 10})}

    Include literals by indexing with ``None``

    >>> make_blockwise_graph(add, 'z', 'i', 'x', 'i', 100, None,  numblocks={'x': (2,)})  # doctest: +SKIP
    {('z', 0): (add, ('x', 0), 100),
     ('z', 1): (add, ('x', 1), 100)}

    See Also
    --------
    dask.array.blockwise
    dask.blockwise.blockwise
    """

    if numblocks is None:
        raise ValueError("Missing required numblocks argument.")
    new_axes = new_axes or {}
    io_deps = io_deps or {}
    argpairs = list(toolz.partition(2, arrind_pairs))

    if return_key_deps:
        key_deps = {}

    if deserializing:
        from distributed.protocol.serialize import to_serialize

    if concatenate is True:
        from dask.array.core import concatenate_axes as concatenate

    # Dictionary mapping {i: 3, j: 4, ...} for i, j, ... the dimensions
    dims = dims or _make_dims(argpairs, numblocks, new_axes)

    # Generate the abstract "plan" before constructing
    # the actual graph
    (coord_maps, concat_axes, dummies) = _get_coord_mapping(
        dims,
        output,
        out_indices,
        numblocks,
        argpairs,
        concatenate,
    )

    # Unpack delayed objects in kwargs
    dsk2 = {}
    if kwargs:
        task, dsk2 = unpack_collections(kwargs)
        if dsk2:
            kwargs2 = task
        else:
            kwargs2 = kwargs

    # Apply Culling.
    # Only need to construct the specified set of output blocks
    output_blocks = output_blocks or itertools.product(
        *[range(dims[i]) for i in out_indices]
    )

    dsk = {}
    # Create argument lists
    for out_coords in output_blocks:
        deps = set()
        coords = out_coords + dummies
        args = []
        for cmap, axes, (arg, ind) in zip(coord_maps, concat_axes, argpairs):
            if ind is None:
                if deserializing:
                    args.append(stringify_collection_keys(arg))
                else:
                    args.append(arg)
            else:
                arg_coords = tuple(coords[c] for c in cmap)
                if axes:
                    tups = lol_product((arg,), arg_coords)
                    if arg not in io_deps:
                        deps.update(flatten(tups))

                    if concatenate:
                        tups = (concatenate, tups, axes)
                else:
                    tups = (arg,) + arg_coords
                    if arg not in io_deps:
                        deps.add(tups)
                # Replace "place-holder" IO keys with "real" args
                if arg in io_deps:
                    # We don't want to stringify keys for args
                    # we are replacing here
                    idx = tups[1:]
                    args.append(io_deps[arg].get(idx, idx))
                elif deserializing:
                    args.append(stringify_collection_keys(tups))
                else:
                    args.append(tups)
        out_key = (output,) + out_coords

        if deserializing:
            deps.update(func_future_args)
            args += list(func_future_args)

        if deserializing and isinstance(func, bytes):
            # Construct a function/args/kwargs dict if we
            # do not have a nested task (i.e. concatenate=False).
            # TODO: Avoid using the iterate_collection-version
            # of to_serialize if we know that are no embeded
            # Serialized/Serialize objects in args and/or kwargs.
            if kwargs:
                dsk[out_key] = {
                    "function": func,
                    "args": to_serialize(args),
                    "kwargs": to_serialize(kwargs2),
                }
            else:
                dsk[out_key] = {"function": func, "args": to_serialize(args)}
        else:
            if kwargs:
                val = (apply, func, args, kwargs2)
            else:
                args.insert(0, func)
                val = tuple(args)
            # May still need to serialize (if concatenate=True)
            dsk[out_key] = to_serialize(val) if deserializing else val

        if return_key_deps:
            key_deps[out_key] = deps

    if dsk2:
        dsk.update(ensure_dict(dsk2))

    if return_key_deps:
        return dsk, key_deps
    else:
        return dsk


def lol_product(head, values):
    """List of list of tuple keys, similar to `itertools.product`.

    Parameters
    ----------
    head : tuple
        Prefix prepended to all results.
    values : sequence
        Mix of singletons and lists. Each list is substituted with every
        possible value and introduces another level of list in the output.

    Examples
    --------
    >>> lol_product(('x',), (1, 2, 3))
    ('x', 1, 2, 3)
    >>> lol_product(('x',), (1, [2, 3], 4, [5, 6]))  # doctest: +NORMALIZE_WHITESPACE
    [[('x', 1, 2, 4, 5), ('x', 1, 2, 4, 6)],
     [('x', 1, 3, 4, 5), ('x', 1, 3, 4, 6)]]
    """
    if not values:
        return head
    elif isinstance(values[0], list):
        return [lol_product(head + (x,), values[1:]) for x in values[0]]
    else:
        return lol_product(head + (values[0],), values[1:])


def lol_tuples(head, ind, values, dummies):
    """List of list of tuple keys

    Parameters
    ----------
    head : tuple
        The known tuple so far
    ind : Iterable
        An iterable of indices not yet covered
    values : dict
        Known values for non-dummy indices
    dummies : dict
        Ranges of values for dummy indices

    Examples
    --------
    >>> lol_tuples(('x',), 'ij', {'i': 1, 'j': 0}, {})
    ('x', 1, 0)

    >>> lol_tuples(('x',), 'ij', {'i': 1}, {'j': range(3)})
    [('x', 1, 0), ('x', 1, 1), ('x', 1, 2)]

    >>> lol_tuples(('x',), 'ijk', {'i': 1}, {'j': [0, 1, 2], 'k': [0, 1]}) # doctest: +NORMALIZE_WHITESPACE
    [[('x', 1, 0, 0), ('x', 1, 0, 1)],
     [('x', 1, 1, 0), ('x', 1, 1, 1)],
     [('x', 1, 2, 0), ('x', 1, 2, 1)]]
    """
    if not ind:
        return head
    if ind[0] not in dummies:
        return lol_tuples(head + (values[ind[0]],), ind[1:], values, dummies)
    else:
        return [
            lol_tuples(head + (v,), ind[1:], values, dummies) for v in dummies[ind[0]]
        ]


def optimize_blockwise(graph, keys=()):
    """High level optimization of stacked Blockwise layers

    For operations that have multiple Blockwise operations one after the other, like
    ``x.T + 123`` we can fuse these into a single Blockwise operation.  This happens
    before any actual tasks are generated, and so can reduce overhead.

    This finds groups of Blockwise operations that can be safely fused, and then
    passes them to ``rewrite_blockwise`` for rewriting.

    Parameters
    ----------
    graph : HighLevelGraph
    keys : Iterable
        The keys of all outputs of all collections.
        Used to make sure that we don't fuse a layer needed by an output

    Returns
    -------
    HighLevelGraph

    See Also
    --------
    rewrite_blockwise
    """
    out = _optimize_blockwise(graph, keys=keys)
    while out.dependencies != graph.dependencies:
        graph = out
        out = _optimize_blockwise(graph, keys=keys)
    return out


def _optimize_blockwise(full_graph, keys=()):
    keep = {k[0] if type(k) is tuple else k for k in keys}
    layers = full_graph.layers
    dependents = reverse_dict(full_graph.dependencies)
    roots = {k for k in full_graph.layers if not dependents.get(k)}
    stack = list(roots)

    out = {}
    dependencies = {}
    seen = set()
    io_names = set()

    while stack:
        layer = stack.pop()
        if layer in seen or layer not in layers:
            continue
        seen.add(layer)

        # Outer loop walks through possible output Blockwise layers
        if isinstance(layers[layer], Blockwise):
            blockwise_layers = {layer}
            deps = set(blockwise_layers)
            io_names |= layers[layer].io_deps.keys()
            while deps:  # we gather as many sub-layers as we can
                dep = deps.pop()

                if dep not in layers:
                    stack.append(dep)
                    continue
                if not isinstance(layers[dep], Blockwise):
                    stack.append(dep)
                    continue
                if dep != layer and dep in keep:
                    stack.append(dep)
                    continue
                if layers[dep].concatenate != layers[layer].concatenate:
                    stack.append(dep)
                    continue
                if (
                    sum(k == dep for k, ind in layers[layer].indices if ind is not None)
                    > 1
                ):
                    stack.append(dep)
                    continue
                if (
                    blockwise_layers
                    and layers[next(iter(blockwise_layers))].annotations
                    != layers[dep].annotations
                ):
                    stack.append(dep)
                    continue

                # passed everything, proceed
                blockwise_layers.add(dep)

                # traverse further to this child's children
                for d in full_graph.dependencies.get(dep, ()):
                    # Don't allow reductions to proceed
                    output_indices = set(layers[dep].output_indices)
                    input_indices = {
                        i for _, ind in layers[dep].indices if ind for i in ind
                    }

                    if len(dependents[d]) <= 1 and output_indices.issuperset(
                        input_indices
                    ):
                        deps.add(d)
                    else:
                        stack.append(d)

            # Merge these Blockwise layers into one
            new_layer = rewrite_blockwise([layers[l] for l in blockwise_layers])
            out[layer] = new_layer

            new_deps = set()
            for k, v in new_layer.indices:
                if v is None:
                    new_deps |= keys_in_tasks(full_graph.dependencies, [k])
                elif k not in io_names:
                    new_deps.add(k)
            dependencies[layer] = new_deps
        else:
            out[layer] = layers[layer]
            dependencies[layer] = full_graph.dependencies.get(layer, set())
            stack.extend(full_graph.dependencies.get(layer, ()))

    return HighLevelGraph(out, dependencies)


def _unique_dep(dep, ind):
    # Append blockwise index information to dependency name
    return dep + "_" + "_".join(str(i) for i in list(ind))


def rewrite_blockwise(inputs):
    """Rewrite a stack of Blockwise expressions into a single blockwise expression

    Given a set of Blockwise layers, combine them into a single layer.  The provided
    layers are expected to fit well together.  That job is handled by
    ``optimize_blockwise``

    Parameters
    ----------
    inputs : List[Blockwise]

    Returns
    -------
    blockwise: Blockwise

    See Also
    --------
    optimize_blockwise
    """
    if len(inputs) == 1:
        # Fast path: if there's only one input we can just use it as-is.
        return inputs[0]

    inputs = {inp.output: inp for inp in inputs}
    dependencies = {
        inp.output: {d for d, v in inp.indices if v is not None and d in inputs}
        for inp in inputs.values()
    }
    dependents = reverse_dict(dependencies)

    new_index_iter = (
        c + (str(d) if d else "")  # A, B, ... A1, B1, ...
        for d in itertools.count()
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )

    [root] = [k for k, v in dependents.items() if not v]

    # Our final results.  These will change during fusion below
    indices = list(inputs[root].indices)
    new_axes = inputs[root].new_axes
    concatenate = inputs[root].concatenate
    dsk = dict(inputs[root].dsk)

    changed = True
    while changed:
        changed = False
        for i, (dep, ind) in enumerate(indices):
            if ind is None:
                continue
            if dep not in inputs:
                continue

            changed = True

            # Change dep name to avoid fusing the same dep
            # (in different iteration orders) into a single
            # subgraph key/dependency
            # (see: https://github.com/dask/dask/issues/8535)
            local_dep = dep if dep == root else _unique_dep(dep, ind)

            # Replace _n with dep name in existing tasks
            # (inc, _0) -> (inc, 'b')
            dsk = {k: subs(v, {blockwise_token(i): local_dep}) for k, v in dsk.items()}

            # Remove current input from input indices
            # [('a', 'i'), ('b', 'i')] -> [('a', 'i')]
            _, current_dep_indices = indices.pop(i)
            sub = {
                blockwise_token(i): blockwise_token(i - 1)
                for i in range(i + 1, len(indices) + 1)
            }
            dsk = subs(dsk, sub)

            # Change new input_indices to match give index from current computation
            # [('c', j')] -> [('c', 'i')]
            new_indices = inputs[dep].indices
            sub = dict(zip(inputs[dep].output_indices, current_dep_indices))
            contracted = {
                x
                for _, j in new_indices
                if j is not None
                for x in j
                if x not in inputs[dep].output_indices
            }
            extra = dict(zip(contracted, new_index_iter))
            sub.update(extra)
            new_indices = [(x, index_subs(j, sub)) for x, j in new_indices]

            # Update new_axes
            for k, v in inputs[dep].new_axes.items():
                new_axes[sub[k]] = v

            # Bump new inputs up in list
            sub = {}
            # Map from (id(key), inds or None) -> index in indices. Used to deduplicate indices.
            index_map = {(id(k), inds): n for n, (k, inds) in enumerate(indices)}
            for ii, index in enumerate(new_indices):
                id_key = (id(index[0]), index[1])
                if id_key in index_map:  # use old inputs if available
                    sub[blockwise_token(ii)] = blockwise_token(index_map[id_key])
                else:
                    index_map[id_key] = len(indices)
                    sub[blockwise_token(ii)] = blockwise_token(len(indices))
                    indices.append(index)
            new_dsk = subs(inputs[dep].dsk, sub)

            # Change new_dsk key to match local_dep
            if dep != local_dep and dep in new_dsk:
                new_dsk[local_dep] = new_dsk.pop(dep)

            # indices.extend(new_indices)
            dsk.update(new_dsk)

    # De-duplicate indices like [(a, ij), (b, i), (a, ij)] -> [(a, ij), (b, i)]
    # Make sure that we map everything else appropriately as we remove inputs
    new_indices = []
    seen = {}
    sub = {}  # like {_0: _0, _1: _0, _2: _1}
    for i, x in enumerate(indices):
        if x[1] is not None and x in seen:
            sub[i] = seen[x]
        else:
            if x[1] is not None:
                seen[x] = len(new_indices)
            sub[i] = len(new_indices)
            new_indices.append(x)

    sub = {blockwise_token(k): blockwise_token(v) for k, v in sub.items()}
    dsk = {k: subs(v, sub) for k, v in dsk.items() if k not in sub.keys()}

    indices_check = {k for k, v in indices if v is not None}
    numblocks = toolz.merge([inp.numblocks for inp in inputs.values()])
    numblocks = {k: v for k, v in numblocks.items() if v is None or k in indices_check}

    # Update IO-dependency information
    io_deps = {}
    for v in inputs.values():
        io_deps.update(v.io_deps)

    return Blockwise(
        root,
        inputs[root].output_indices,
        dsk,
        new_indices,
        numblocks=numblocks,
        new_axes=new_axes,
        concatenate=concatenate,
        annotations=inputs[root].annotations,
        io_deps=io_deps,
    )


@_deprecated()
def zero_broadcast_dimensions(lol, nblocks):
    """
    >>> lol = [('x', 1, 0), ('x', 1, 1), ('x', 1, 2)]
    >>> nblocks = (4, 1, 2)  # note singleton dimension in second place
    >>> lol = [[('x', 1, 0, 0), ('x', 1, 0, 1)],
    ...        [('x', 1, 1, 0), ('x', 1, 1, 1)],
    ...        [('x', 1, 2, 0), ('x', 1, 2, 1)]]

    >>> zero_broadcast_dimensions(lol, nblocks)  # doctest: +SKIP
    [[('x', 1, 0, 0), ('x', 1, 0, 1)],
     [('x', 1, 0, 0), ('x', 1, 0, 1)],
     [('x', 1, 0, 0), ('x', 1, 0, 1)]]

    See Also
    --------
    lol_tuples
    """
    f = lambda t: (t[0],) + tuple(0 if d == 1 else i for i, d in zip(t[1:], nblocks))
    return homogeneous_deepmap(f, lol)


def broadcast_dimensions(argpairs, numblocks, sentinels=(1, (1,)), consolidate=None):
    """Find block dimensions from arguments

    Parameters
    ----------
    argpairs : iterable
        name, ijk index pairs
    numblocks : dict
        maps {name: number of blocks}
    sentinels : iterable (optional)
        values for singleton dimensions
    consolidate : func (optional)
        use this to reduce each set of common blocks into a smaller set

    Examples
    --------
    >>> argpairs = [('x', 'ij'), ('y', 'ji')]
    >>> numblocks = {'x': (2, 3), 'y': (3, 2)}
    >>> broadcast_dimensions(argpairs, numblocks)
    {'i': 2, 'j': 3}

    Supports numpy broadcasting rules

    >>> argpairs = [('x', 'ij'), ('y', 'ij')]
    >>> numblocks = {'x': (2, 1), 'y': (1, 3)}
    >>> broadcast_dimensions(argpairs, numblocks)
    {'i': 2, 'j': 3}

    Works in other contexts too

    >>> argpairs = [('x', 'ij'), ('y', 'ij')]
    >>> d = {'x': ('Hello', 1), 'y': (1, (2, 3))}
    >>> broadcast_dimensions(argpairs, d)
    {'i': 'Hello', 'j': (2, 3)}
    """
    # List like [('i', 2), ('j', 1), ('i', 1), ('j', 2)]
    argpairs2 = [(a, ind) for a, ind in argpairs if ind is not None]
    L = toolz.concat(
        [
            zip(inds, dims)
            for (x, inds), (x, dims) in toolz.join(
                toolz.first, argpairs2, toolz.first, numblocks.items()
            )
        ]
    )

    g = toolz.groupby(0, L)
    g = {k: {d for i, d in v} for k, v in g.items()}

    g2 = {k: v - set(sentinels) if len(v) > 1 else v for k, v in g.items()}

    if consolidate:
        return toolz.valmap(consolidate, g2)

    if g2 and not set(map(len, g2.values())) == {1}:
        raise ValueError("Shapes do not align %s" % g)

    return toolz.valmap(toolz.first, g2)


def _make_dims(indices, numblocks, new_axes):
    """Returns a dictionary mapping between each index specified in
    `indices` and the number of output blocks for that indice.
    """
    dims = broadcast_dimensions(indices, numblocks)
    for k, v in new_axes.items():
        dims[k] = len(v) if isinstance(v, tuple) else 1
    return dims


def fuse_roots(graph: HighLevelGraph, keys: list):
    """
    Fuse nearby layers if they don't have dependencies

    Often Blockwise sections of the graph fill out all of the computation
    except for the initial data access or data loading layers::

      Large Blockwise Layer
        |       |       |
        X       Y       Z

    This can be troublesome because X, Y, and Z tasks may be executed on
    different machines, and then require communication to move around.

    This optimization identifies this situation, lowers all of the graphs to
    concrete dicts, and then calls ``fuse`` on them, with a width equal to the
    number of layers like X, Y, and Z.

    This is currently used within array and dataframe optimizations.

    Parameters
    ----------
    graph : HighLevelGraph
        The full graph of the computation
    keys : list
        The output keys of the computation, to be passed on to fuse

    See Also
    --------
    Blockwise
    fuse
    """
    layers = ensure_dict(graph.layers, copy=True)
    dependencies = ensure_dict(graph.dependencies, copy=True)
    dependents = reverse_dict(dependencies)

    for name, layer in graph.layers.items():
        deps = graph.dependencies[name]
        if (
            isinstance(layer, Blockwise)
            and len(deps) > 1
            and not any(dependencies[dep] for dep in deps)  # no need to fuse if 0 or 1
            and all(len(dependents[dep]) == 1 for dep in deps)
            and all(layer.annotations == graph.layers[dep].annotations for dep in deps)
        ):
            new = toolz.merge(layer, *[layers[dep] for dep in deps])
            new, _ = fuse(new, keys, ave_width=len(deps))

            for dep in deps:
                del layers[dep]
                del dependencies[dep]

            layers[name] = new
            dependencies[name] = set()

    return HighLevelGraph(layers, dependencies)
