def bold(func):
    def wrapper():
        return "<bold>" + func() + "</bold>"
    return wrapper


def italic(func):
    def wrapper():
        return "<italic>" + func() + "</italic>"
    return wrapper

def uppercase(something):
    def wrapper():
        original_method = something() # it looks like 'something' is a placeholder
        modified_method = original_method.upper()
        return modified_method
    return wrapper

def before(func):
    def before():
        return "Before" + func()
    return before

def after(func):
    def wrapper():
        return func() + "after"
    return wrapper
    
@after
@before   
@uppercase
@italic            
@bold              
def greet():
    return "hello"


# print(greet())

def trace(func):
    def wrapper(*args, **kwargs):
        print(f"TRACE: calling {func.__name__}()"
        f"with {args}, {kwargs}")

        origina_result = func(*args, **kwargs)

        print(f"TRACE: {func.__name__}()"
        f"returned {origina_result!r}")

        return origina_result
    return wrapper



@trace
def say(name, line):
    return f"{name}: {line}"

print(say("Jane", "Hey there!"))