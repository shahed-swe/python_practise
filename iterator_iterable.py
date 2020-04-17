list1 = [1,2,3,4,5] #list is an iterable object
# list can't directly call by next function
# first of all we have to make it an iterator then we can call it via next() function

# for i in list1:
#     print(i)

# here is this loop we made this type of thing

i = iter(list1)
print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

# next(i) #this time it will show you an error

# but do we know map() function give us an iterator object?
# ok let's see
l1 = list(range(1,11))

def square(take):
    return [i**2 for i in take]

list2 = map(int, square(l1))
print(list2)
# for i in list2:
#     print(i)


print(next(list2))
print(next(list2))
print(next(list2))
print(next(list2))
print(next(list2))