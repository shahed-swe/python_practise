# string indexing
name = "Shahed"
# here 
# S > 0, -6
# h > 1 , -5
# a > 2, -4
# h > 3, -3
# e > 4, -2
# d > 5, -1

print(name[3],name[-3])
print(name[-1])
# string slicing
# syntax of string sliciing - [start argument : stop argument]
print(name[2:6])
print(name[-3:5])
print(name[:])
print(name[1:6])
print(name[:3])

# step argument
# syntax - [start argument : stop argument: step argument]
print(name[::-1])
print(name[-1::-1])
print(name[6:2:-1])

#methods in python
# len() -- count length of any string or list
print(len("Shahed")) #without storing data in a variable
lenght = len("Shahed Talukder")
print(lenght)
# lower() -- make string in lower case
name = input()
name = name.lower()
print(name)
# upper() -- make string in upper case
name = input()
name = name.upper()
print(name)
# title() -- make string in title case(first item in upper case and other in lower case)
name = input()
name = name.title()
print(name)
# count() -- to count similer type caracter
string = input("Enter a full string")
char = input("Enter a character to count")
c_char = string.count(char)
print(c_char)

#exercise
# user_name = input("Enter your name:")
# u_char = input("Enter a character:")
user_name, u_char = input("Enter your string and char").split(",")
print(f"character count: {user_name.lower().count(u_char.lower())}")
user_name = user_name.lower()
u_char = u_char.lower()
u_count = user_name.count(u_char)
# for i in range(len(user_name)):
#     if u_char == u_char.lower() or u_char == u_char.upper():
#         u_count = user_name.count(u_char)
#         u_count += 1
print(f"Length of your string is: {len(user_name)}")
print(f"character count: {u_count}")

#strip methos
#lstrip() - remove left side spaces
#rstrip() - remove right side spaces
#strip() - remove all spaces
name = "       Shahed           "
dots = "........."
print(name+dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
# replace method
print(name.replace(" ","")+dots)

#taking input using strip or replace method
user_name,u_char = input().split(",")
print(f"Length of the string: {len(user_name.strip())}")
print(f"Character count: {user_name.lower().count(u_char.strip().lower())}")

#using of replace() method
s1 = "Shahed Talukder Is now in a vacation"
s2 = s1.replace(" ","_")
print(f"Using of replace() method: {s2}")
#we can change a string with that replace method also like that
s3 = s1.replace("Is","was")
print("Replacing: {}".format(s3))
#if we have same kind of string in some where in string then we can change it by numbering
s1 = "Shahed is on a sports team. And he is going to do something"
s2 = s1.replace("is","was",1)
print(f"Replacing: {s2}")
#if we want to change another (is) then we have to do that
s2 = s1.replace("is","was",2)
print("Replacing: {0}".format(s2))

#using of find() method
s1 = "Shahed is on a sports team. And he is going to do something"
s2 = s1.find("is")
print(f"Findin string: {s2}")
#after defining position of (is)
s2 = s1.find("is", 8) #this will start finding after position 8..where first (is) is in position 7
print("Finding string: {}".format(s2))

#example of find() method
s1 = "Shahed is on a sports team. And he is going to do something"
s2  = s1.find("is")
print("Finding string: {}".format(s2))
print("Finding string: {}".format(s1.find("is",s2+1)))

#using of center() method
#center usually prints a character (left or right) in a string
#example
name = "Shahed"
l = len(name)
new_name = name.center(l+2,"*")
print(new_name)
new_name = name.ljust(l+2,"*")
new_name = name.rjust(l+2,"*")

# upper()
# lower()
# title()
# find()
# count()
# strip()
# lstrip()
# rstrip()
#replace()
name = "The quick brown fox jumps over the lazy dog"
print(text.upper())
print(text.lower())
print(name.title())

string = "Suppose you have to do this early and you have to the same work again you to"

print(name.find("fox"))
print(string.find("to",18, 45))
print(string.find("you",12))
print(string.count("you",10,41))
text = "           Shahed           "
print(string.strip())
print(text.lstrip())
print(text.rstrip())
print(text.strip())

print(string.replace(" ","",3))