
# Pygal's country codes are stored in a module called i18n
# short for: internationalization
# dictionary COUNTRIES contains two-letter country codes as keys
# and coutnry names as values

# NOTE: i18n module wasa removed in pygal-2.0.0
# so found in pygal_maps_world plugin
# pip install pygal_maps_world
# then can access as
from pygal.maps.world import COUNTRIES
## from pygal.i18n import COUNTRIES

# prints out all the country codes and countries in world?
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

def get_country_code(country_name):
    # return 2 digit country code for given country

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if country not found
    return None

print(get_country_code('Andorra'))
print(get_country_code('Iceland'))
# this will return none
print(get_country_code('Taiwan'))
# This will actually return TW ...
print(get_country_code('Taiwan, Province of China'))