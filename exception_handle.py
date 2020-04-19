# exception handling
# try except else finally

# while True:
#     try:
#         age = int(input("Enter your age:")) #if error occurs then no variable will be made for it
#         break #to stop the loop if right input is given
#     except ValueError:
#         print("Invalid input")
#     else:
#         print(f"user input {age}")
#         break
#     finally:
#         print('finally blocks....')


# if age < 18:
#     print("You can't play this game")
# else:
#     print("you can play this game")


def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError as err:
        # print("please don't divide by zero")
        print(err)
    except TypeError as err:
        # print('Please input numbers only')
        print(err)


print(divide(2,5))
print(divide(5,0))
print(divide('4',2))