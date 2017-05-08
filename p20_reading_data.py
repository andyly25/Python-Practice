# now to write program to read list back to memory
# this is a simple way of sharing data between two programs

import json

#made sure to read from same file wrote to
filename = 'numbers.json'
#now we just need to read from file for our purpose this time
with open(filename) as f_obj:
    #use json.load() to load info stored in file into the var numbers
    numbers = json.load(f_obj)
print(numbers)