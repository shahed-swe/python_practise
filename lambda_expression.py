# def add(a,b):
#     return a + b

add = lambda a,b: a + b
multiply = lambda a,b : a * b

summation = lambda *args : sum(args)


if __name__ == '__main__':
    print(add(12,34))
    print(multiply(12,34))
    l1 = [1,2,3,4,5]
    print(summation(*l1))

# basically we use lambda expression in some built in functions
# like: map, reduce,filter etc

new = lambda a : a % 2 == 0
print("Summation is :{}".format(new(12)))

last_char = lambda string : string[-1]
print(last_char("shahed"))

rev_str = lambda string : string[::-1]
print(rev_str('shahed'))

length = lambda string : len(string) < 5
print("length of the string {}".format(length("shahed talukder")))

length = lambda string : "Greatest" if len(string) > 5 else "Smallest"
print(length("Shhaed Talukder"))


new_list = []
for i in range(3):
    new_list.append(i+1)
    new_list.append([i for i in range(i*3+1,i*3+3+1)])
    
print(new_list)


#palindrom checker with lambda expression
palindrom_check = lambda string : string  == string[::-1]

name = input("Enter your name:")
print(palindrom_check(name))

