#let's make another program with python funtion
def add_two(a,b):
    return a + b
def sub_two(a,b):
    return a - b
def mul_two(a,b):
    return a * b
def div_two(a,b):
    return a / b

if __name__ == '__main__':
    x = int(input("Enter an integer number:"))
    y = int(input("Enter an integer number:"))
    sum_total = add_two(x,y)
    sub_total = sub_two(x,y)
    mul_total = mul_two(x,y)
    div_total = div_two(x,y)
    
    print("Summation of two number: {}".format(sum_total))
    print(f"Subtraction of two number: {sub_total}")
    print("Multiplication of two number: {0}".format(mul_total))
    print("Division of two number:",round(div_total,4))


def rev_string(string):
    return string[::-1]

if __name__=='__main__':
    name = input("Enter your name:")
    print("Your name in reverse: {}".format(rev_string(name)))


#even odd check with python function
def check_even_odd(num_check):
    if num_check % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == '__main__':
    num = int(input("Enter an integer number: "))
    check = check_even_odd(num)
    print("Your number is {}".format(check))

#we can bypass number and string with same parameter in python

def check_even_odd(num_check):
    if num_check % 2 == 0:
        return "even"
    return "odd"

if __name__ == '__main__':
    num = int(input("Enter an integer number: "))
    check = check_even_odd(num)
    print("Your number is {}".format(check))

#another two process with bolian value
def is_check(num):
    if num % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    num = int(input("Enter an integer number:"))
    check = is_check(num)
    print("Your number is {}".format(check))


#most simple process
def is_check(num): #here num is parameter
    return num % 2 == 0
    
if __name__ == '__main__':
    num = int(input("Enter an integer number:"))
    check = is_check(num) #here num is argument
    print("Your number is {}".format(check))

#we can return any value without any parameter in python
def name():
    return "Shahed"

if __name__ == '__main__':
    name = name()
    print(f"My name is: {name}")


def find_greater(x,y):
    if x > y:
        return x
    return y

if __name__ == '__main__':
    a = int(input("Enter an integer number: "))
    b = int(input("Enter another integer number: "))
    c = find_greater(a,b)
    print("{} is biggest number".format(c))


def find_greater_number(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    return z

if __name__ == '__main__':
    a,b,c = map(int, input().split())
    greatest = find_greater_number(a,b,c)
    print(f"The greatest number is: {greatest}")


#we can call a function inside a function like c language
def find_greatest():
#     c = find_greater_number(23,34,25)
    d = find_greater(find_greater_number(23,34,25),35)
    return d

if __name__ == '__main__':
    x = find_greatest()
    print("Greatest number is: {}".format(x))

#funtion exercise 2
def is_palindrome(string):
    st = string[::-1]
    if string == st:
        return True
    return False

def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

def is_palindrome(string):
    return string == string[::-1]


if __name__ == '__main__':
    string = input("Enter a string: ")
    check = is_palindrome(string)
    print("Palindriom is : {}".format(check))



#fibonacchi number printing in python
def fibonacchi_seq(n):
    a , b = 0 , 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a,b, end = " ")
        for i in range(n - 2):
            a, b = b , a + b
            print(b, end = " ")

if __name__ == '__main__':
    fibonacchi_seq(25)

# default parameter
#An special value (None)
#we can make default parameter in last parameter only
# without making last parameter as default we can't make any other parameter as default parameter
def My_Info(name,age = None,address = 'Unknown'): #here if we don't make address as default parameter we can't make age 
#     as default parameter
    print("My name is: {}".format(name))
    print("My age is: {}".format(age))
    print("My address is: {}".format(address))

if __name__ == '__main__':
    My_Info("Shahed",24,"Tangail")


#scope variable
x = 9

def change_value():
    global x
    x = func()
    return x

def func():
    i = int(input())
    return i

if __name__ == '__main__': 
    print("Value of x: {}".format(x))
    z = change_value()
    print("Value of x: {}".format(z))
    print("value of x: {}".format(x))