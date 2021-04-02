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
        original_method = something()  # it looks like 'something' is a placeholder
        modified_method = original_method.upper()
        return modified_method
    return wrapper


def before(func):
    def before():
        return "Before" + func()
    return before


@before
@uppercase
@italic             # First the function get decorator from the top
@bold               # Then the next one : top to bottom
def greet():
    return "hello"


print(greet())
