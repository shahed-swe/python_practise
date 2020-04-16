#while loop in python
i = 0 #initialization
while i < 10: #condition
    print("Hello world!!") 
    i += 1 #statement

#sum of ten numbers using while loop
total = 0
i = 0
while i < 3:
    num = int(input())
    total += num
    i += 1
print("Sum of {} numbers is: {}".format(i,total))

#exercise 1:
total = 0
n = int(input("Enter a natural number: "))
i = 0
while i < n and n > -1:
    num = int(input("Enter an integer number:"))
    total += num
    i += 1
print(f"Sum of {i} numbers is: {total}")

#exercise 2:
n1 = input()
i = 0
sum_number = 0
while i < len(n1):
    n2 = n1[i]
    n2 = int(n2)
    sum_number += n2 
    i +=1
print("Sum of the digits: {}".format(sum_number))


string = input("Enter any string: ")
i = 0
temp = ""
while i < len(string):
    if string[i] not in temp:
        temp += string[i]
        print("{} : {}".format(string[i],string.count(string[i])))
    i += 1

#let's talk about infinite loop
#we do this by mistake
#while(1):
    #print("Hello World!!") example of infinite loop
# i = 0
# while i < 10:
#     print("Hello world!!")
#     i = i + 0
#this is also an example of infinite loop..
# we are not running this in my ide becase this will crash if i run this

#another infinite loop which will be made by use normally
# while True:
#     print("Hello world!!!")