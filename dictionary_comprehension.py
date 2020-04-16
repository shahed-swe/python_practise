# without dictionary comprehension
dictionary = {}
for i in range(1,11):
  if i % 2 == 0:
    dictionary[i] = "even"
  else:
    dictionary[i] = "odd"
for i,j in dictionary.items():
  print("{} : {}".format(i,j))

#with dictionary comprehension
dictionary = {i : "even" if i % 2 == 0 else "odd" for i in range(1,11)}
print(dictionary)
for i,j in dictionary.items():
  print("{} : {}".format(i,j))

