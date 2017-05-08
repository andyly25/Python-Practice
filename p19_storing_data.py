import json

numbers = [2,3,5,7,11,13]

# choosing a filename to store list of numbers
filename = 'numbers.json'
#open the file in write mode, allow json to write data to file
with open(filename, 'w') as f_obj:
    #json.dump function to store list numbers in the file
    json.dump(numbers, f_obj)

