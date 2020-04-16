def decorator_function(any_function): #this type of decorator will be use if function doesn't return anything
    def wrapper_function(*args, **kwargs):
        print("this is awesome function")
        any_function(*args,**kwargs)
    return wrapper_function

def decorator_func(any_function): #this type of decorator will be used if function return something when it been called
    def wrapper_function(*args,**kwargs):
        print("this is awesome function")
        return any_function(*args, **kwargs)
    return wrapper_function
# var = decorator_function(func)
# var(7)

@decorator_function
def func(a):
    print(f"this is function with argument {a}")
# both of the above are same

func(7)
@decorator_func #this is right and we will get the perfect output
def add(a,b):
    return a + b

@decorator_function #this won't work and we will get None as output if we run this function
def add2(a,b):
    return a+b

print(add(2,3))


print(add2(2,3))