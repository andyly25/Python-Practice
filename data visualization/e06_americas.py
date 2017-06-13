import pygal

# no more world map, renamed to be
from pygal.maps.world import World
# make an instance of the World class
wm = World()
## wm = pygal.Worldmap()
wm.title = 'North, Central, and South America'
# we use add to take in a label and list of country codes.
# each call to add sets a new color for set of countries 
# for NA, we pass a dictionart as 2nd arg instead of list.
# dict has country codes as keys and pop as values. This auto shades
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])

# this is how we create a svg file that contains the chart, open in browser
wm.render_to_file('e06_americas1.svg')
