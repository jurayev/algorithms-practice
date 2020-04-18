import time
import functools


def profile(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        elapsed = time.perf_counter() - start

        inner.__total_time__ += elapsed
        inner.__n_calls__ += 1

        return result

    inner.__total_time__ = 0
    inner.__n_calls__ = 0
    return inner
