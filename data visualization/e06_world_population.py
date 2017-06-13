'''
json file is one long Python list, with each item being a dictionary.
For the example I'm using, there are four keys:
a country name, country code, year, and value for population.
'''

# first load json modulae to load data properly from file
import json
from e06_countries import get_country_code

#load data into list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# loop through each item in pop_data where each item is a dictionary.
# We then store each dictionary into pop_dict.
#print the 2010 population for each country
for pop_dict in pop_data:
    # if we find the keyword 2010 in year, we store rest of the data we need
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # a ValuerError would appear since can't directly turn a string that 
        # has a decimal into an integer so we do this below to solve it.
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else: 
            print('ERROR - ' + country_name)
            
        # print(country_name + ": " + str(population))