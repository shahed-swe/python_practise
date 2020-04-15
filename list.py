#list 
number = [1,2,3,4]
print(number)
words = ["shahed","ashik","azad","rajib"]
print(words)
mixed = [1,2,3,"shahed","ashik",0.56,1.56,None] #None is not as same as 0 value
print(mixed)
print(number[1])
print(words[:2])
print(mixed[-1])
#we can change list element directly
mixed[2] = 'two'
print(mixed)
mixed[1:] = 'two' #if we want to change every element from position [1]
print(mixed)
mixed[1:] = ['three','four']
print(mixed) #if we want to store another element separately


#adding data to list
name = ['shahed','ashik']
print(name)
name.append('rajib')
print(name)
new_name = [] #a list without any elements
new_name.append('rajib')
new_name.append('ashik')
print(new_name)

#more methods to add data in list
#insert method helps to add element in position in list
name = ['shahed','ashik']
name.insert(1,'rajib')
name.insert(0,'azad')
print(name)
#join or concatenate two list
fruits = ['jackfruit','mango','pineapple']
animals = ['hilsha','magpi','tiger']
new_list = fruits + animals
print(new_list)
fruits.extend(animals) #this will extend two list
print(fruits)
print(animals)
animals.append(fruits) #this will insert a list into another list
print(animals)
for i in range(len(animals)):
    print(animals[i])
#print(animals[3][0]) #to print another elements of another list
for i in range(len(animals)):
    print(animals[3][i])
name.insert(1,fruits)
print(name)

# removing or deleting elements from list
# pop method
fruits.pop() #if we don't pass any argument this method will delete last element
print(fruits)
fruits.pop(2)#after passing argument this will delete indexed postion element
print(fruits)
#remove method()
#this helps to remove element if we don't know the position of that elemet like
fruits.remove('hilsha')
print(fruits)

another_list = ['shahed','ashik','azad','shahed','ashik','rajib','noman']
another_list.remove('ashik') #if you have two elements with same value this will delete first element
print(another_list)

#in keyword with list
another_list = ['shahed','ashik','azad','shahed','ashik','rajib','noman']
if 'apple' in fruits:
    print("apple is present")
else:
    print("apple is not present")


#some more list methods
#count
#sort method
#sorted function
#reverse
#clear
#copy
another_list = ['shahed','ashik','azad','shahed','ashik','rajib','noman']
a = another_list.count('shahed') #count method can count how many elements are exist with the same name
print(a)
another_list.sort() #this sort the whole list elements in ascending order or alphabetic order
print(another_list)
num = [12,1,3,5,17,21]
num.sort()
print(num)
#if we want just print the elements in sorted order but don't want to sort the elements
num = [12,1,3,5,17,21]
print(sorted(num)) #this just print your elements in sorted order
print(num)
#clear method is used to delete the whole list
num.clear()
print(num) #thsi delete all elements from a list
num = [12,1,3,5,17,21]
num1 = num.copy()
print(num1)


#some more list methods
#count
#sort method
#sorted function
#reverse
#clear
#copy
another_list = ['shahed','ashik','azad','shahed','ashik','rajib','noman']
a = another_list.count('shahed') #count method can count how many elements are exist with the same name
print(a)
another_list.sort() #this sort the whole list elements in ascending order or alphabetic order
print(another_list)
num = [12,1,3,5,17,21]
num.sort()
print(num)
#if we want just print the elements in sorted order but don't want to sort the elements
num = [12,1,3,5,17,21]
print(sorted(num)) #this just print your elements in sorted order
print(num)
#clear method is used to delete the whole list
num.clear()
print(num) #thsi delete all elements from a list
num = [12,1,3,5,17,21]
num1 = num.copy()
print(num1)


#is vs equal in python list comparison
f1 = ['orange','apple','pear']
f2 = ['banana','kiwi','apple','banana']
f3 = ['orange','apple','pear']
print(f1 == f2)
print(f1 == f3)
#normal pratise exercise
another_list = ['shahed','ashik','azad','shahed','ashik','rajib','noman',['rabit','horse','orange']]
a_list = [1,2,3,4,5,[2,5,6]]
count = 0
for i in another_list:
    if type(another_list) is list:
        for j in i:
            print(j)
    else:
        print(i)
#problem still not found

another_list = ['shahed','ashik','azad','shahed','ashik','rajib','noman',['rabit','horse','orange']]
another_list = str(another_list)
another_list = another_list.replace("[","").replace("]","").replace("'","")
another_list = another_list.split(",")
print(another_list)
for i in another_list:
    print(i)

#split() and join method
name,age = input("Enter your name and age:").split() #split method
#now let's talk about join method
n = int(input("Enter how many elements you want to enter: "))
all_in = []
for i in range(n):
    elem = input("Enter your elements: ")
    all_in.append(elem)
print(name)
print(age)
# join method
new = "\n".join(all_in)
print(new)

#list vs array
#we can add only same type of element in array
#we can add different type of element in list
# python have array module to use like c or c++ named numpy
# javascript array = python list /flexible


# difference between list and string
# strings are immutable
# list are mutable
#like
s = "shahed"
s.title()
print(s) #here varible of s is not changing but
s = ["shahed","ashik","azad"]
s.sort() #here we see that the list is in order..means a function named sort is changing
s.append("rajib")
print(s)
#so we can not change in string but we can change in list by calling function

#looping in list
list1 = ["jackfruit","mango","lichi",None,345,56.7,"arabic"]
for i in list1: #using for loop
    print(i)
i = 0
while i < len(list1): #using while loop
    print(list1[i])
    i+=1

#looping in list
list1 = ["jackfruit","mango","lichi",None,345,56.7,"arabic"]
for i in list1: #using for loop
    print(i)
i = 0
while i < len(list1): #using while loop
    print(list1[i])
    i+=1

#more about join method
#convert list to string
user_info = input("Enter your name and age:").split(" ")
print(user_info[0])
print(user_info[1])
print(','.join(user_info))