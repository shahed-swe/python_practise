import json
import sys


# # filename = 'username.json'
# filename = sys.argv[1]

# try:
#     with open(filename) as file:
#         username = json.load(file)
# except FileNotFoundError:
#     username = input("whats your username:")
#     with open(filename,'w') as file:
#         json.dump(username, file)
#         print("well remeber you when you come back {}!".format(username))
# else:
#     print(f"welcome back {username}")


def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username
    
def store_user():
    username = greet_user()
    if username:
        print('welcome back'+username)
    else:
        username = input("whats your username?")
        filename = 'username.json'
        with open(filenamme,'w') as file:
            json.dump(username, file)
            print("we will remember you when you come back "+ username + "!")

store_user()