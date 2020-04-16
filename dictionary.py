#what is dictionary
#an unorderd collection of data in key : value pair

user = {'name' : 'shahed', 'age' : 24}
print(user)

user = dict(name = 'Shahed', age = 24)
print(user)

print(user['name'],user['age'])

user_info = dict(
    user_name = 'shahed',
    email = 'shahedtalukder51@gmail.com',
    age = 21,
    address = 'East Adalotpara,Tangail',
    fav_movie = ['end_game','infinity war','dark web']
)


print(user_info)

user_info = dict(
    user1 = dict(
        user_name = "shahed",
        age = 21,
        password = 'asdfasdf'
    ),
    user2 = dict(
        user_name = "ashik",
        age = 22,
        password = 'asfdasdf'
    ),
    user3 = dict(
        user_name = 'azad',
        age = 23,
        password = 'asdfasdf'
    )
)

print(user_info)

# deep dictionary
user_info = {}
name = input("Enter your name:")
age = input("Enter your age:")
password = input("Enter your password:")
count = 1
string = 'user'
user_name = string + str(count)
user_info = {
    user_name : {
        'name' : name,
        'age' : age,
        'password' : password
    }
}
print(user_info)

#lets make it deep
#mr google..

user_info = {}
new_user = {}
num = int(input("Enter how many times you want to enter your information:"))
count = 1
string = 'user'
for i in range(num):
  fname = input("Enter your First name:")
  lname = input("Enter your Last name:")
  age = input("Enter your age:")
  address = input("Enter your address:")
  user_number = string+str(count)
  user_info = {
    user_number : {
        'fname' : fname,
        'lname' : lname,
        'age' : age,
        'address' : address
    }
  }
  print("Inserted successfully")
  new_user.update(user_info)
  count+=1
print(new_user)

# in keyword in dictionary and iterations in dictionary

user_info = dict(
    name = 'shahed',
    age = 24,
    fav_movies = ['end_game','infinite war','hellowen'],
    fev_tunes = ['hello','faded','on my way']
)


#check if key exist in dictionary
if 'name' in user_info:
  print("Key present")
else:
  print('Not present')
  
#check if value exist in dictionary

#add update and pop
user_info = dict(
    name = 'shahed',
    age = 24,
    fav_movies = ['end_game','infinite war','hellowen'],
    fev_tunes = ['hello','faded','on my way']
)
popped_item = user_info.pop('fev_tunes')
print(f"Popped item is {popped_item}")
print(type(popped_item))
user_info['address'] = 'khagan bazar'
print(user_info)
popped_item = user_info.popitem()
print(popped_item)
print(type(popped_item))

#updating key and element
user_info = dict(
    name = 'shahed',
    age = 24,
    fav_movies = ['end_game','infinite war','hellowen'],
    fev_tunes = ['hello','faded','on my way']
)

more_info = dict(
    state = 'Dhaka',
    hobbies = ['singing','dancing']
)

user_info.update(more_info)
print(user_info)

#method fromkeys to create dictionary

d = dict(
    name = 'Unknown',
    age = 'Unknown'
)
# fromkeys() function has two attribute.exp: fromkeys(key, value)
d = dict.fromkeys(['name','age','height'],'unknown')
print(d)
d = dict.fromkeys(range(1,11),'9')
print(d)

#get method
user_info = dict(
    name = 'shahed',
    age = 24,
    fav_movies = ['end_game','infinite war','hellowen'],
    fev_tunes = ['hello','faded','on my way']
)

print(user_info.get('name')) #better
user_info.clear()
print(user_info)

user_info = d.copy()
print(user_info)

# verify key or not
user = dict(
    name = 'shahed',
    age = 24
)

print(user.get('name','not a key!')) #return the value of name (shahed)
print(user.get('names','not a key!')) #return message 'not a key!'

# dictionary key can't be repeated
user = {
    'name' : 'shahed',
    'age' : 24,
    'age' : 34
}

print(user)

#cube finder
def cube_finder(num):
  cube = {}
  for i in range(1,num+1):
    cube[i] = i**3
  return cube

# letter counting exercise 1
if __name__ == '__main__':
  num = int(input("Enter an integer number:"))
  print("Dictionary is:")
  print(cube_finder(num))

  def word_counter(string):
  word = {}
  for i in string:
    word[i] = string.count(i)
  return word

if __name__  == '__main__':
  name = input("Enter your name:")
  print(word_counter(name))


# letter counting exercise 2
def word_counter(string):
  word = {}
  for i in string:
    word[i] = string.count(i)
  return word

if __name__  == '__main__':
  name = input("Enter your name:")
  dictionary = word_counter(name)
  for i,j in dictionary.items():
    print("{} : {}".format(i,j))
  #printing keys
  for i in dictionary:
    print(i)


