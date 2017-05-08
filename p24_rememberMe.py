# Here we are going to improve the code to look nicer
# hence term Refactoring

import json

def get_stored_username():
    # get stored username if available
    filename = "text_files/username.json"
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    # prompts for new username
    filename = "text_files/username.json"
    username = input("What is your name? ")
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
    return username

def greet_user():
    """Greets the username"""
    username = get_stored_username()
    if username:
        # exercise asking if username is right
        reply = input("Is " + username + " the right username? (y or n) ")
        if reply == 'n':
            get_new_username()
            greet_user()
        else:
            print("Welcome back " + username)
    else: 
        username = get_new_username()
        print("Come back soon " + username)
        


greet_user()