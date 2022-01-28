import ctypes

def install_perf_counters(perf_counters):
    libcfiddle = _load_libcfiddle()

    for pc in perf_counters:
        if isinstance(pc, str):
            libcfiddle.add_perf_counter(ctypes.c_char_p(pc.encode()))
        else:
            raise ValueError("Expected instance of 'str' not {type(pc).__name__}.")

def are_perf_counters_available():
    return bool(_load_libcfiddle().are_perf_counters_available())


def clear_perf_counters():
    _load_libcfiddle().clear_perf_counters()


def _load_libcfiddle():
    return  ctypes.CDLL("libcfiddle.so")

