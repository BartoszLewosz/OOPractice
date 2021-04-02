
def uppercase(f):
    def wrapper():
        orig_result = f()
        mod_result = orig_result.upper()
        return mod_result
    return wrapper


def null_decorator(func):
    return func

@uppercase
def greet():
    return "hello"


greet_func = null_decorator(greet)

print(greet())
# # >>> hello


@null_decorator
def greet():
    return "Hello"


print(greet())
# # >>> Hello
