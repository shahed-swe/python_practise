#set
list1 = [1,2,3,4,5,6,7,2,4,1,4,6,7,5,0]
print(list1)
s = set(list1)
print(s)
sl = list(s)
print(sl)
s.add(10)
print(s)
s.remove(4)
print(s)
s.discard(11)
print(s)


set1 = {1,3,5,6,7}
set2 = {3,2,9,7}
union_set = set1 | set2
intersection_set = set1 & set2
print(union_set)
print(intersection_set)