numbers = [3,4,5,1,2,6,7,6,8]
#filter function
#process 1
def is_even(a):
  return a%2 == 0

def is_odd(a):
  return a%2 != 0

evens = list(filter(is_even, numbers))
odds = list(filter(is_odd, numbers))
print(evens,odds)

#process 2
evens = list(filter(lambda a: a%2 == 0, numbers))
odds = list(filter(lambda a: a%2 != 0, numbers))
print(evens,odds)

#process 3
evens = [i for i in numbers if i % 2 == 0]
odds = [i for i in numbers if i % 2 != 0]
print(evens,odds)

