# def square(a):
#   return a**2
#one method without including it into map

square = lambda a : a**2

numbers = [1,2,3,4]
print(map(square, numbers))

square = list(map(square, numbers))
print(square)

def square(a):
  return a**2

new_num = []
for i in numbers:
  new_num.append(square(i))
  
print(new_num)
# here is the end of new func

# multiple process to count length of the string
names = ['shahed','ashik','azad','thankyou']

#process 1
length = list(map(lambda string : len(string), names))
print(length)

#process 2
def length(string):
  return len(string)

num = []
for i in names:
  num.append(length(i))
print(num)

#process 3
num = [len(i) for i in names]
print(num)

#process 4
length = list(map(len, names))
print(length)


