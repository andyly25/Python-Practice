# now we combine the logic of 21 and 22 into this file
# 24 will be a refactored form of the code

import json

#load the username if it has been stored previously
#Otherwise, prompt for the usrname and store it.

filename = 'text_files/username.json'

try:
    #attempt to open the file
    with open(filename) as f_obj:
        username = json.load(f_obj)
# if the file hasn't been made we make one since the error will occur
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("Come back soon " + username + "!")
# if this happens, this means there was already a file made
else: 
    print("Welcome back " + username + "!")