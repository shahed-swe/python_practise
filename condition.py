#if statement
#syntax of if statement
#if <condition>:
    #statement
#example
if int(input("Enter your age: ")) >= 14:
    print("You are above 14")
# or
age = int(input("Enter another age: "))
if age >= 18:
    print(f"You are above {14}.")

#pass statement
#this use to pass the condition in if or else statement
#example
age = int(input("Enter your age: "))
if age == 18:
    pass
elif age > 18:
    print("You are above 18")
else:
    print("You are under 18")

#using random number
import random
print(random.randint(1,10))
# syntax of random package using
#random.randint(starting point,endpoint)

#exercise with nested if else
import random
winner_number = random.randint(10,20)
guess_number = int(input("Enter the number you have guessed: "))
if guess_number == winner_number:
    print("YOU WIN!!!")
else:
    if guess_number < winner_number:
        print("too low!!")
    else:
        print("too high!!")

#and, or operator in python
user_name = "shahed"
pass_word = "32100505"
if (input("Enter your user name:") == user_name) and (input("Enter your password:") == pass_word):
    print("You are now logged in!!!")
else:
    print("Your input is wrong!!!")
#that was for (and) operator
#now let's see (or) operator
if (input("Enter your user name:") == user_name or (input("Enter your password:") == pass_word)):
    print("Your are now logged in!!!")
else:
    print("Your input is wrong!!!")

#exercise of (and,or) operator
user_name = input("Enter your user name:")
user_age = int(input("Enter your age:"))
if (user_name[0] == 'A' or user_name[0] == 'a') and user_age >= 10:
    print("You can watch coco movie!!")
else:
    print("Sorry, you can't watch coco movie!!")

age = int(input("Enter your age:"))
if age >= 1 and age <=3:
    print("Your ticket price is tottaly free!!")
elif age >= 4 and age <= 10:
    print("Your ticket price is 150 tk only!!")
elif age >= 11 and age <= 60:
    print("Your ticket price is 250 tk only!!")
elif age > 60:
    print("Your ticket price is 200 tk only!!")
else:
    pass



#in keyword working with in
#in keyword search for a character in string like
user_name = "Shahed Talukder"
char = input()
if char in user_name:
    print("{} is in {}".format(char,user_name))


#check empty or not(important)
name = input("Enter you name here:")
if name: #True if string is not empty
    print("Your name is: {}".format(name))
else:
    print("You did't enter your name yet!!!")


