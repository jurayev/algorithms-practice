import functools


def uppercase(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        return f(*args, **kwargs).upper()
    print("This is the first")
    return inner


def split(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        return f(*args, **kwargs).split()
    print("This is the last")
    return inner


@split
@uppercase
def say(phrase: str) -> str:
    """This will say a phrase"""
    return phrase


print(say(phrase="Hello there!"))
print(say("my name is"))
print(say(phrase="Hey"))
print(say.__name__)
print(say.__doc__)
