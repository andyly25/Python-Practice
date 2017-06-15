'''
First attempt: grabbing the provided country code and the key,
    Doesn't seem to work maybe because the examples I followed utilized
    2-letter country codes? So let's just go back to grabbing country names
    then converting into 2-letters
Second attempt: yep... it works now after using country names and converting 
    into 2-letters.

here's the countries not found:
    Aruba not found
    Andorra not found
    American Samoa not found
    Antigua and Barbuda not found
    Bermuda not found
    Curacao not found
    Cayman Islands not found
    Dominica not found
    Faroe Islands not found
    Micronesia, Fed. Sts. not found
    Gibraltar not found
    Grenada not found
    Greenland not found
    Isle of Man not found
    Not classified not found
    Kiribati not found
    St. Kitts and Nevis not found
    Liechtenstein not found
    St. Martin (French part) not found
    Monaco not found
    Marshall Islands not found
    Northern Mariana Islands not found
    Nauru not found
    Palau not found
    San Marino not found
    South Sudan not found
    Sint Maarten (Dutch part) not found
    Seychelles not found
    Turks and Caicos Islands not found
    Tuvalu not found
    British Virgin Islands not found
    Kosovo not found

If I wasn't lazy, I'd add them all to the map.

114 28 7
'''

import csv

from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from pygal.maps.world import World

# from iso3166 import countries
from e06_countries import get_country_code

# def get_country_code(country_name):
#     # return 2 digit country code for given country

#     for code, name in countries.items():
#         if name == country_name:
#             return code
#     # if country not found
#     return None

# store filename of file we're working with then open it
filename = 'worldUnemployment.csv'
# a UnicodeDecodeError appeared so I'll add utf-8 for encoding 
with open(filename, newline='', encoding='utf-8') as f:
    # then pass file as arg to create reader object associated with file
    reader = csv.reader(f)
    # next() returns the next line in file, in this case only once for header

    # inelegant, but let's skip first 3 rows
    # Maybe I can just do a while loop that keeps looping until I 
    # the next line contains row[0] == "Country Name" or something like that
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    header_row = next(reader)
    # print(header_row)

    # Now to grab country code and data from year 2016
    # ccDict = {}
    # for row in reader:
    #     # grab data from col 1 and then data from col 60
    #     ccDict['Country Code'] = row[1]
    #     ccDict['Value'] = row[60]

    # for keys, values in ccDict.items():
    #     print(keys, values)

    myDict = {}
    # myDict = {rows[1]:float(rows[60]) for rows in reader}
    # print(myDict)
    # intDict = dict(k, float(v)) for k, v in myDict.items()

    for rows in reader:
        try:
            country_name = rows[0]
            code = get_country_code(country_name)
            # key = rows[1]
            value = int(float(rows[60]))
        except:
            # print(key + " not found")
            print(country_name + ' not found')
        else:
            # myDict[key] = value
            myDict[code] = value

# print (myDict)
   
# Group the countries into 3 population levels
cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
for cc, pop in myDict.items():
    if pop <10:
        cc_pop1[cc] = pop
    elif pop < 20:
        cc_pop2[cc] = pop
    else:
        cc_pop3[cc] =pop

# see how many countries in each level.
print(len(cc_pop1), len(cc_pop2), len(cc_pop3))


# add some styling using RotateStyle, takes in a hex color
# first two nums are red, next 2 is green, last 2 is blue
wm_style = RS('#336699', base_style=LCS)

# make an instance of the World class
wm = World(style=wm_style)

wm.title = 'World Unemployment 2016, by Country'
# pass dictionary of cc and pop values
# wm.add('2010', cc_populations)
wm.add('0-10', cc_pop1)
wm.add('10-20', cc_pop2)
wm.add('>20', cc_pop3)

wm.render_to_file('e06_world_unemployment.svg')
 
