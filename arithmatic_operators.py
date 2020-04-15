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