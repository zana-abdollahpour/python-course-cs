'''
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''

from functools import wraps


def once(fn):
    count = 0

    @wrpas(fn)
    def inner(*args, **kwargs):
        if count > 0:
            return
        count = 1
        return fn(*args, **kwargs)
    return inner


def just_once(fn):
    fn.is_called = False

    def inner(*args):
        if not (fn.is_called):
            fn.is_called = True
            return fn(*args)
    return inner
