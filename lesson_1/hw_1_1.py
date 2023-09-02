def outer(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

def div(a, b):
    return a / b

var = outer(div)

print(var(1,2))