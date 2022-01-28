"""
A threaded shared-memory scheduler

See local.py
"""
import atexit
import multiprocessing.pool
import sys
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from threading import Lock, current_thread

from . import config
from .local import MultiprocessingPoolExecutor, get_async
from .system import CPU_COUNT
from .utils_test import add, inc  # noqa: F401


def _thread_get_id():
    return current_thread().ident


main_thread = current_thread()
default_pool = None
pools = defaultdict(dict)
pools_lock = Lock()


def pack_exception(e, dumps):
    return e, sys.exc_info()[2]


def get(dsk, result, cache=None, num_workers=None, pool=None, **kwargs):
    """Threaded cached implementation of dask.get

    Parameters
    ----------

    dsk: dict
        A dask dictionary specifying a workflow
    result: key or list of keys
        Keys corresponding to desired data
    num_workers: integer of thread count
        The number of threads to use in the ThreadPool that will actually execute tasks
    cache: dict-like (optional)
        Temporary storage of results

    Examples
    --------

    >>> dsk = {'x': 1, 'y': 2, 'z': (inc, 'x'), 'w': (add, 'z', 'y')}
    >>> get(dsk, 'w')
    4
    >>> get(dsk, ['w', 'y'])
    (4, 2)
    """
    global default_pool
    pool = pool or config.get("pool", None)
    num_workers = num_workers or config.get("num_workers", None)
    thread = current_thread()

    with pools_lock:
        if pool is None:
            if num_workers is None and thread is main_thread:
                if default_pool is None:
                    default_pool = ThreadPoolExecutor(CPU_COUNT)
                    atexit.register(default_pool.shutdown)
                pool = default_pool
            elif thread in pools and num_workers in pools[thread]:
                pool = pools[thread][num_workers]
            else:
                pool = ThreadPoolExecutor(num_workers)
                atexit.register(pool.shutdown)
                pools[thread][num_workers] = pool
        elif isinstance(pool, multiprocessing.pool.Pool):
            pool = MultiprocessingPoolExecutor(pool)

    results = get_async(
        pool.submit,
        pool._max_workers,
        dsk,
        result,
        cache=cache,
        get_id=_thread_get_id,
        pack_exception=pack_exception,
        **kwargs,
    )

    # Cleanup pools associated to dead threads
    with pools_lock:
        active_threads = set(threading.enumerate())
        if thread is not main_thread:
            for t in list(pools):
                if t not in active_threads:
                    for p in pools.pop(t).values():
                        p.shutdown()

    return results
