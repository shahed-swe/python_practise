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
def nums2(n):
    list1 = []
    for i in range(1,n+1):
        list1.append(i)
    return list1

numbers = nums(1000000000000)
t1 = t.time()

numbers = nums2(10000)
t2 = t.time()

print(t2-t1)
# as you can see generator basically generates its datas only one time and takes so short time then list

# let's go for some example