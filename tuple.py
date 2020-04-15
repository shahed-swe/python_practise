#tuples intro
#we can't insert,update,or delete any kind of element from tuple
#we can only find the index number of elemnet
#we can slice tuple elements
#we can count the number of elements



example  = ("one","two","three")
days  = ("sunday","monday")
print(example,days)
print("Type of exmple is {}".format(type(example)))

#tuple with one element
nums = (1) # is not a tuple...this will show use that this is just an integer value
print(type(nums))
nums = (1,) #now this is a tuple
print(type(nums))

#tuple without parathesis

guiters = "shahed", "ashik","azad"
print(type(guiters))

#tuple unpacking
x,y,z = (guiters)
print(x)
print(y)
print(z)

#tuple with list
new_elem = ("new1","new2",["new3","new4"])
new_elem[2].pop()
print(new_elem)
new_elem[2].append("shahed")
print(new_elem)

#when a funtion return two values it returns a tuple object from funtion

def sum_mul(i1,i2):
  add = i1 + i2
  mul = i1 * i2
  return add,mul

if __name__ == '__main__':
  print(type(sum_mul(2,3)))
  print(sum_mul(5,4))
  #as it is returning a tuple we can assign with two different variable
  x,y = sum_mul(6,7)
  print(x,y)


tp1 = tuple(range(1,11))
print(len(tp1))
print(min(tp1))
print(max(tp1))
print(sum(tp1))