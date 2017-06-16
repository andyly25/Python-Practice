
# import modules
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# call get() and pass the url to receive a response that has an attribute
# status code telling if successful or not
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
# since info is a JSON format we convert into a Python dictionary
response_dict = r.json()
# this represents total num of Python reps
print("Totale repositories:", response_dict['total_count'])

# Explore information about repositories.
# 'items' is a list containing a num of dicts, each with data for each rep
# so we store these dicts into repo_dicts
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Examine the first repository
# results:
# Totale repositories: 1754785
# Repositories returned: 30
repo_dict = repo_dicts[0]


# create 2 empty lists. We need name of each project to label bars

names, plot_dicts = [], []
# loop througha all dict in repo_dicts
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Here we make a dictionary for each project
    # yeah.. a mistake from examples, you'll get the AttributeError:
    # 'NoneType' blah blah so for the label, wrap around with str.
    # let's also add clickable links
    plot_dict = {
        'value' : repo_dict['stargazers_count'],
        'label' : str(repo_dict['description']),
        'xlink' : repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# make a visualization
# base on a darkshade of blue, also pasee LCS for base_style
my_style = LS('#333366', base_style=LCS)

# REFINING PYGAL CHARTS
# make an instance of Pygal's config class
my_config = pygal.Config()
# moved out from below and added up here
my_config.x_label_rotation = 45
my_config.show_legend = False
# se font size for title, and minor and major labels.
# minor is project names and most numbers on y-axis. 
# Major are on y-axis that marks off increments of 5k stars
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# shorten longer project names to 15 characters
my_config.truncate_label = 15
# hide horizontal lines on graph
my_config.show_y_guides = False
# set custom width to allow chart use more of space on browser
my_config.width = 1000


# make a simple Bar and pass in style. set rotation of labels along x axis
# to be 45 degrees and hide the legend
chart = pygal.Bar(my_config, style=my_style)
chart.force_uri_protocol = 'http'
chart.title = 'Most starred Python Projects on GitHUb'
chart.x_labels = names

# since we don't need this data series to be labeled we pass empty string
chart.add('', plot_dicts)
chart.render_to_file('e07_python_repos2.svg')