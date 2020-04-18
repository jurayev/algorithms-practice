import functools

def singleton(f):

    called = False

    @functools.wraps(f)
    def inner(*args, **kwargs):
        nonlocal called
        if not called:
            called = True
            return f(*args, **kwargs)
    return inner

@singleton
def login(usr, passwd):
    """Logs in a user"""
    print(f"Logged in with Username: '{usr}', Password: '{passwd}'")

login("Yuriy", "myPasswd")
login("Yuriy1", "myPasswd1")