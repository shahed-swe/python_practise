# iterator vs iterables

numbers = [1,2,3,4] #iterables
squares = map(lambda a: a**2, numbers) #iterator
print(squares)
# for iterables
# print(next(numbers)) //list object is not an iterator..
new = iter(numbers)
print(iter(numbers))
print(next(new))
print(next(new))
print(next(new))
print("\n")
#for iterators
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))