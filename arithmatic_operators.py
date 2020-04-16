# n = int(input("Enter an integer number:"))
# m = int(input("Enter another integer number:"))
n,m = map(int, input().split())
# normal arithmatic operators
print("{} + {} = {}".format(n,m,n+m))
print("{} - {} = {}".format(n,m,n-m))
print("{} * {} = {}".format(n,m,n*m))
print("{} / {} = {}".format(n,m,n/m))
print("{} % {} = {}".format(n,m,n%m))
print("{} ** {} = {}".format(n,m,n**m))
print("{} // {} = {}".format(n,m,n//m))


# round function

print("{} / {} = {} ".format(100,3,round(100/3, 2)))

# snake case writing
my_name = "Shahed"
# camel case writing
myName = "Shahed"

print("{}\n{}".format(my_name, myName))

# string and int

# always remember that we can not add , substract or device string with integer but we can multiply string with int
take = "Shahed" * 2
print(take)

# output will be ShahedShahed

# floating point
#type convertion string formating
n1 = 36
n2 = 24
print("Number one: {0:f}\nNumber two: {1:f}".format(
    n1, n2))  # --> for full decimal digits
print("Number one: {0:.2f}\nNumber two: {1:.3f}".format(
    n1, n2))  # -->for selected decimal digits
#double type
print("Result: {}".format(100/3))
#float type
print("Result: {0:.2f}".format(100/3))
# spacing in python

#Spacing in string formating
#Note. spacing starts after 3
print("My age is: {0:4d}".format(21))  # --> for two space
print("My age is: {0:2d}".format(21))  # -->for zero space
#left chevron and right chevron in string
print("My name is: {0:>4} and my id is: {1:<4}".format("Shahed", "173-25-258"))
#caret symbol(^) using
#must use caret symbol > the string length
print("{0:*^9s}".format("Shahed"))
print("{0:*^7s}".format("Shahed"))


#operator in python
name = "sha"
name = name + "hed"
print(name) #we cam add two string..but can't add two different type of data typed varibles value like
age = 21
# print(name + age) #this will show error
#but we can add int type and float type data like
age2 = 22
print(age + age2)
# we can also operators like that way
age += age2
print(age) #this will like same as before like
age -= 2
print(age)
age *= 2
print(age)