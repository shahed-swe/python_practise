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

#list inside list
count = 0
matrix = [[1,2,3],[4,5,6],[5,6,9]]
for i in matrix:
  count += 1
  print(i)
print("items are: ",count)
count = 0
for j in matrix:
  for i in j:
    print(i)
    count += 1
print("Items are:",count)
print(matrix[2][0])


#range function
numbers = list(range(1,11))
print(numbers)
popped_item = numbers.pop()
print(numbers)
print(popped_item)
print("Position of 6 is:",numbers.index(6))
# negative list
def negative_list(l1):
  negative = []
  for i in l1:
    negative.append(-i)
  return negative

if __name__ == '__main__':
  num = list(range(1,10))
  print("Negative list: {}".format(negative_list(num)))

# square list
def square_list(l1):
  square = []
  for i in l1:
    square.append(i*i)
  return square

if __name__ == '__main__':
  num = list(range(1,10))
  print(f"Square numbers: {square_list(num)}")

# reverse list
def reverse_list(list1):
  reverse = []
  for i in range(len(list1)):
    new = list1.pop()
    reverse.append(new)
  return reverse

if __name__ == '__main__':
  numbers = list(range(1,11))
  print(numbers)
  print("Reverse list: {}".format(reverse_list(numbers)))

# reverse list element
def reverse_list_elem(list2):
  new_list = []
  for i in list2:
    new_list.append(i[::-1])
  return new_list


if __name__ == '__main__':
  elements = ['abc','def','ghi']
  print("Reversed Elements list is: {}".format(reverse_list_elem(elements)))


# even odd separet list
def seperate_list(list1):
  even = []
  odd = []
  new_list = []
  for i in list1:
    if i % 2 == 0:
      even.append(i)
    else:
      odd.append(i)
  new_list = [odd,even]
  return new_list

if __name__ == '__main__':
  num = list(range(1,11))
  print("Even Odd list is: {} ".format(seperate_list(num)))

# common list
def common_list(list1,list2):
  new_list = []
  for i in list1:
    for j in list2:
      if i == j:
        new_list.append(i)
  return new_list

if __name__ == '__main__':
  l1 = [1,2,6,7]
  l2 = [1,6,3,9]
  print("Common list: {}".format(common_list(l1,l2)))

# common list
def common_list(list1,list2):
  new_list = []
  for i in list1:
    if i in list2:
      new_list.append(i)
  return new_list

if __name__ == '__main__':
  l1 = [1,2,6,7]
  l2 = [1,6,3,9]
  print("Common list: {}".format(common_list(l1,l2)))


  #min and max function in list
def differ(list1):
  return max(list1) - min(list1)

if __name__ == '__main__':
  numbers = [23,11,4,56,45]
  print("Difference is: {}".format(differ(numbers)))
  print(min(numbers))
  print(max(numbers))


# list count
def list_count(list1):
  count = 0
  for i in list1:
    if type(i) == list:
      count += 1
  return count

if __name__ == '__main__':
  list1 = [1,2,5,[4,5,6],[5,8,7]]
  print("Total list element: {}".format(list_count(list1)))

# difference between append and extend
list1 = [1,2,3]
list1.append("Shahed")
list1.append([1,5,6])
list1.extend([6,4,9])
list2 = [2,9,5]
print(list1)
print(list1 + list2)



