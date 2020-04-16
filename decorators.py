# you have to have a complete understanding of functions
# first class function / closures
# then finally we will learn about decorators

def square(a):
    '''this function will return square to you'''
    return a**2

s = square
print(s(2))

print(s.__doc__)
print(square.__doc__)

l = list(range(1,5))

# passing function inside a function
def my_map(func,take):
    new_list = []
    for item in take:
        new_list.append(func(item))
    return new_list

def my_map2(func, take):
    return [func(item) for item in take]

print(my_map(square, l))

print(my_map2(square, l))

print(my_map2(lambda a: a**3, l))

# outer function is returning inner function indirectly
def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func

# outer function is returning inner function directly
def outer_func2():
    def inner_func2():
        print('inside innner func')
    return inner_func2()

var = outer_func()
var()

var2 = outer_func2()


def outer_func3(msg):
    def inner_func3():
        print(f"message is {msg}")
    return inner_func3

var = outer_func3("Shahed Talukder")
var()

def func4(take):
    def square(num):
        return num**take
    return square

var = func4(2)
print(var(33))
