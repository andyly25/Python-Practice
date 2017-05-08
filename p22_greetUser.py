# this is part 2 of the separate files, will be combined into 23

import json

filename = 'text_files/username.json'

with open(filename) as f_obj:
    # json.load reads info and then stores into the variable
    username = json.load(f_obj)
    # now we can use that information
    print("Welcome back " + username)