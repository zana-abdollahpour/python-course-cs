from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Running {fn.__name__}")
        t_start = time()
        fn(*args, **kwargs)
        t_end = time()
        print(f"your fn ran in {t_end-t_start} seconds")
    return wrapper
