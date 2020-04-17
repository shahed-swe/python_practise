# create your first generator with generator function
# generator function
# generator comprehension

# generator only generate only one data each time 
import time as t

def nums(n):
    for i in range(1,n+1):
        yield(i)

# print(nums(10))
# for number in nums(10):
#     print(number)
# def nums2(n):
#     list1 = []
#     for i in range(1,n+1):
#         list1.append(i)
#     return list1

# numbers = nums(1000000000000)
# t1 = t.time()

# numbers = nums2(10000)
# t2 = t.time()

# print(t2-t1)
# as you can see generator basically generates its datas only one time and takes so short time then list

# let's go for some example

def even_number(get):
    for i in range(1,get+1):
        if i%2 == 0:
            yield i

for i in even_number(10):
    print(i)

for i in (i for i in range(1,11) if i%2==0): #hahahaha you didn't get that right?
    print(i)

# ok let's see

nums = (i for i in range(1,11)) #run this code
print(nums)

# if you have already run this code then let's make a generator object which will be field with odd numbers

nums = (i for i in range(1,11) if i % 2 != 0)
for i in nums:
    print(i)

# this is the result