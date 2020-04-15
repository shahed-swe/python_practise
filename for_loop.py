#for loop in python
#syntax of for loop
for i in range(6):
    print("Hello world: {}".format(i))
for i in range(1,6):
    print("Shahed: {}".format(i))

#example of for loop
total = 0
for i in range(1,11):
    total+=i
    #print("{}".format(i))
print(f"Sum of all: {total}")

#another example of for loop
total = 0
n = int(input("Enter an integer number: "))
for i in range(1,n+1):
    total += i
print(f"Sum of all: {total}")

total = 0
n = input()
for i in range(len(n)):
    total += int(n[i])
print("Total of that string: {}".format(total))

string = input("Enter your name: ")
i = 0
temp = ""
for i in range(len(string)):
    if string[i] not in temp:
        temp += string[i]
        print("{} : {}".format(string[i],string.count(string[i])))


#break and continue keyword
#we use break keyword to break the loop
# example of break
for i in range(1,11):
    if i == 6:
        break
    print("Value of i {}".format(i))
#example of continue
print("\n")
for i in range(1,11):
    if i == 5:
        continue
    print("Value of i {}".format(i))
#here (value of i 5) will not be printed because of continue statement

#modifying number gussing game
import random
w_num = random.randint(1,100)
g_num = int(input("Guess a number between 1 and 100:"))
count = 1
while True:
    if w_num == g_num:
        print("you win, and you guessd this number in {} time".format(count))
        break
    elif g_num > w_num:
        print("Too high!!")
    else:
        print("Too low")
    g_num = int(input("Guess again: "))
    count += 1



#solution from video
import random
w_num = random.randint(1,100)
g_num = int(input("Guess a number between 1 and 100:"))
game_over = False
guess = 1
while not game_over:
    if g_num == w_num:
        print(f"you win, and you guessed this number in {guess} times")
        game_over = True
    else:
        if g_num < w_num:
            print("Too low!!")
            guess += 1
            g_num = int(input("Guess again: "))
        else:
            print("Too high!!")
            guess += 1
            g_num = int(input("Guess again: "))



#DRY principle
# DRY - don't repeat yourself
import random
w_num = random.randint(1,100)
g_num = int(input("Guess a number between 1 and 100:"))
game_over = False #if game_over false
guess = 1
while not game_over:
    if g_num == w_num:
        print(f"you win, and you guessed this number in {guess} times") #for winners
        game_over = True
    else:
        if g_num < w_num:
            print("Too low!!")
        else:
            print("Too high!!")
        guess += 1
        g_num = int(input("Guess again: ")) #input again

#step in for loop
#syntax of for loop with step argument
#for i in range(start argument, stop argument, step argument)
#example
for i in range(1,11,2):
    print(i)
#now let's work with negative numbers
for i in range(-1,-11,-3):
    print(i)


#for loop and string
name = "Shahed"
for i in name:
    print(i)
#string is iterable in python

#example of stirng with for loop
string = input("Enter any integer number:")
total = 0
for i in string:
    total += int(i)
print("sum of that integer number is: {}".format(total))


