import math

from dask.system import CPU_COUNT
from dask.utils import factors


def nprocesses_nthreads(n=CPU_COUNT):
    """
    The default breakdown of processes and threads for a given number of cores

    Parameters
    ----------
    n : int
        Number of available cores

    Examples
    --------
    >>> nprocesses_nthreads(4)
    (4, 1)
    >>> nprocesses_nthreads(32)
    (8, 4)

    Returns
    -------
    nprocesses, nthreads
    """
    if n <= 4:
        processes = n
    else:
        processes = min(f for f in factors(n) if f >= math.sqrt(n))
    threads = n // processes
    return (processes, threads)
