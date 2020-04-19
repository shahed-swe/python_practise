# exception handling
# try except else finally

try:
    age = int(input("Enter your age:")) #if error occurs then no variable will be made for it
except:
    print("Invalid input")

if age < 18:
    print("You can't play this game")
else:
    print("you can play this game")