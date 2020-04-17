from functools import wraps

def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper_function(*args,**kwargs):
            if (all([type(i) == data_type for i in args])):
                return function(*args,**kwargs)
            else:
                print("Invalid Argument or data type")
        return wrapper_function
    return decorator


@only_data_type_allow(str)
def join_string(*args):
    string = ''
    for i in args:
        string += i
    return string

@only_data_type_allow(int)
def summation(*args):
    total = 0
    for i in args:
        total += i
    return total


if __name__ == '__main__':
    print(join_string('Shahed', ' Talukder'))
    print(summation(1,2,3,4,5))