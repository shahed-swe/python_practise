import json
def get_stored_username():
    """if username available"""
    filename = 'username.json'
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    '''prompt user for a new username'''
    username = input("what's your username?")
    filename = 'username.json'
    with open(filename,'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    '''printing username'''
    username = get_stored_username()
    if username:
        print('welcome back '+ username + '!')
    else:
        username = get_new_username()
        print("we will remember you when you come back {} !".format(username))

greet_user()