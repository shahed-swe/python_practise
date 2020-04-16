# intro to arguments means (args*)
# make flexible function
# *operator
# *args

def all_elem(*args):
  print(args)
  print(type(args))
  
def all_sum(*args):
  total = 0
  for i in args:
    total += i
  return total

if __name__ == '__main__':
  all_elem(2,3,4,5)
  print(all_sum(2,5,6,7,8,9))


#we can't write parameter after *arg
def sum_multy(a,b,*args):
  total = 1
  for i in args:
    total *= i
  return total+a+b

if __name__ == '__main__':
  count = sum_multy(27,8,4,5,6,7,8)
  print(count)


# *args with list
def multiply_nums(*args):
  mul = 1
  for i in args:
    mul *= i
  return mul

if __name__ == '__main__':
  num2 = [2,3,4]
  print(type(multiply_nums(2,5,4)))
  print(type(multiply_nums(*num2)))
  print(multiply_nums(2,3,4))
  print(multiply_nums(*num2)) #unpack the list elements first for arguments


#without list comprehension
def power_set(num,*args):
  new_list = []
  for i in args:
    new_list.append(i**num)
  return new_list

if __name__ == '__main__':
  set = [1,2,3,4,5]
  print(power_set(2,*set))

# with list comprehension
def power_set(num,*args):
    if(len(args) < 1):
        return "no value has been given inside arguments"
    else:
        return [i**num for i in args]
if __name__ =='__main__':
    list1 = [1,2,3,4,5,6]
    print(power_set(2,*list1))

# another method
def power_set(num, *args):
    if args:
        return [i**num for i in args if i % 2 == 0]
    return "no values to unpack for calculation"

if __name__ == '__main__':
    list1 = list(range(1,11))
    print(power_set(2, *list1))


#**kwargs implementation

def func(**kwargs):
  for i,j in kwargs.items():
    print("{} : {}".format(i,j))
  
if __name__ == '__main__':
  func(name = "shahed",age = "21")

#another
def func(n,**kwargs):
  for i,j in kwargs.items():
    print("{} : {}".format(i,j))
  print(n)
    
if __name__ == '__main__':
  func("Hello",name = "Shahed",age = "21")


#dictionary unpacking
def dict_unpacking(**kwargs):
  for i,j in kwargs.items():
    print("{} : {}".format(i,j))
if __name__ == '__main__':
  new_dict = dict(
      name = "Shahed",
      age = "21",
      address = "khagan"
  )
  print(new_dict)
  dict_unpacking(**new_dict)

#default param
def func(name = 'unknown',age = 24):
  print(name)
  print(age)
  
func()
func("shahed")
func("shahed",22)

# capital string
def capital_str(l1,**kwargs):
  if kwargs.get('reverse_str') == True:
    return [name[::-1].title() for name in l1]
  else:
    return [name.title() for name in l1]
if __name__ == '__main__':
  list1 = ['shahed','ashik']
  print(capital_str(list1))
  print(capital_str(list1, reverse_str = True))


