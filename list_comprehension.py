#list comprehension

#create a list of squares from 1 to 10
square = [i**2 for i in range(1,11)]
print(square)

#negative number list with list comprehension
negative = [-i for i in range(1,11)]
print(negative)

# even number list using list comprehension
even = [i for i in range(1,11) if i % 2 == 0]
#odd number list using list comprehension
odd = [i for i in range(1,11) if i % 2 != 0]

print(even)
print(odd)
#first letter using list comprehension
name = ['shahed','ashik','rajib','koli']
first_letter = [i[0] for i in name]
print(first_letter)

#without function
list1 = ['abc','def','ghi']
new = [i[::-1] for i in list1]
print(new)

#with funtion
# def reverse_list(list1):
#   new = [i[::-1] for i in list1]
#   return new

def reverse_list(list2):
  return [i[::-1] for i in list2]

if __name__ == '__main__':
  l1 = ['abc','def','ghi','jkl']
  print("Reversed List elements are:")
  print(reverse_list(l1))

def finder(list1):
  l2 = [i for i in l1 if type(i) == int or type(i) == float]
  return l2

if __name__ =='__main__':
  l1 = [True,False,1,2.0,5,1.0,'shahed']
  print(finder(l1))

#without list comprehension
def differ(list1):
  new_list = []
  for i in list1:
    if i % 2 == 0:
      new_list.append(i*2)
    else:
      new_list.append(-i)
  return new_list

if __name__ == '__main__':
  list1 = list(range(1,11))
  print(differ(list1))

#with list comprehension
def differ(list1):
  new_list = [i*2 if i % 2 == 0 else -i for i in list1]
  return new_list

if __name__ == '__main__':
  list2 = list(range(1,11))
  print(differ(list2))

# nested list with list comprehension
nested_comp = [[i for i in range(1,4)] for j in range(3)]
print(nested_comp)

#list comprehension
new_list = [list(range(n*3+1,n*3+3+1)) for n in range(3)]
print(new_list)

# dictionary comprehension
square = {num : num **2 for num in range(1,11)}
print(square)
for i,j in square.items():
  print("Square of {} is {}".format(i,j))

# count word from string again
name = "Shahed Talukder"
word_count = {cnt : name.count(cnt) for cnt in name}
for i,j in word_count.items():
  print("{} : {}".format(i,j))

