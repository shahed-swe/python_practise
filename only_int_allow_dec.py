from functools import wraps

def only_int_allow(function):
    @wraps(function)
    def wrapper_function(*args,**kwargs):
        if (all([type(i) == int for i in args])):
            return function(*args,**kwargs)
        else:
            print("Invalid Argument or data type")
    return wrapper_function


@only_int_allow
def summation(*args):
    return sum(args)

if __name__ == '__main__':
    print(summation(1,2,3,4,[1,2,3]))