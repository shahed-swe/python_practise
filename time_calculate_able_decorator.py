from functools import wraps
import time as t

def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        t1 = t.time()
        returned_val = any_function(*args,**kwargs)
        t2 = t.time()
        print("Total execution time is: {}".format(t2-t1))
        return returned_val
    return wrapper_function



@decorator_function
def summation(*args):
    total = 0
    for i in args:
        total += i
    return total


if __name__ == '__main__':
    list1 = [1,2,3,4,5,6]
    val = summation(*list1)
    print(val)