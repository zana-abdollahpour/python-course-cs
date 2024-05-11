from functools import wraps


def be_polite(fn):
    def wrapper():
        print("Hi dear friend!")
        print(f"your result is {fn()} :)")
        print("Have a nice day!")
    return wrapper


@be_polite
def greet(): return "Gigidi"


greet()


def shout(fn):
    @wraps
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def lol(): return "lol!"


def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if (args[0] != val):
                return f"first arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner
