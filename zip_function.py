#zip function
user_id = ['user1','user2','user3']
names = ['shahed','siam','ashik']
age = [21,23,24]

print(zip(user_id,names))
details = zip(user_id,names,age)
print(next(details))
for i in details:
  print(i)
  

# directly converting to dictionary
fall = [('a',1),('b',2),('c',3)]
print(fall)
print(dict(fall))

l = [(1,2),(3,4),(5,6),(7,8)]
l1,l2 = zip(*l)
print(list(l1))
print(list(l2))



#zip products packing
l1 = [1,2,3,4]
l2 = [2,4,5,6]

new_zip = list(zip(l1,l2))
print(new_zip)

#unpacking
l1,l2 = list(zip(*new_zip))
print(l1,l2)

# collecting max value from two list
l1 = [1,5,3,4]
l2 = [2,4,2,6]
new_list = []
for pair in zip(l1,l2):
  new_list.append(max(pair))
  
print(new_list)

hell = [min(pair) for pair in zip(l1,l2)]
print(hell)