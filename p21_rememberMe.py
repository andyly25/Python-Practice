# Saving and reading User - generated Data
# This is part 1 and will be combined into 23

import json

#takes in user input
username = input("What is your name? ")

filename = 'text_files/username.json'
with open(filename, 'w') as f_obj:
    # passing json.dump username and file to store into file
    json.dump(username, f_obj)
    # print message indicating success
    print("Hurry and come back " + username + "! ")

