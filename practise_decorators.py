from functools import wraps

def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        print("you are calling {} function".format(any_function.__name__))
        print(any_function.__doc__)
        return any_function(*args,**kwargs)
    return wrapper_function


@decorator_function
def add(a,b):
    '''this is the main function from where i am calling the wrapper function to operate'''
    return a+b
print(add(2,3))
