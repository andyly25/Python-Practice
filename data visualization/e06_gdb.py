import json

from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from pygal.maps.world import World

from e06_countries import get_country_code

# Load data into list
file = 'gdp.json'
with open(file) as f:
    gdp_data = json.load(f)

# build a dict of gdp data
cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] =='2014':
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)

        if code:
            cc_gdps[code] = gdp

# group countries into 3 gdp levels
gdp1, gdp2, gdp3 = {}, {}, {}
for cc, gdp in cc_gdps.items():
    if gdp < 5000000000:
        gdp1[cc] = round(gdp/1000000000)
    elif gdp < 50000000000:
        gdp2[cc] = round(gdp/1000000000)
    else:
        gdp3[cc] = round(gdp/1000000000)

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'Global GDP 2014, by Country in billions USD'
wm.add('0-5bn', gdp1)
wm.add('5bn-50bn', gdp2)
wm.add('>50bn', gdp3)

wm.render_to_file('e06_gdp.svg')