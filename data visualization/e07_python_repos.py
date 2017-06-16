'''
First results is:
    Status code: 200
    dict_keys(['incomplete_results', 'total_count', 'items'])

    NOTE: For more complex API calls, programs should check the 
    incomplete_results value
'''

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

# TO know what info available through API is to read documentation
# or by examining the info through code
# RESULTS:
# Selected info about 1st rep:
# Name: awesome-python
# Owner: vinta
# Stars: 35028
# Repository: https://github.com/vinta/awesome-python
# created 2014-06-27T21:00:06Z
# updated: 2017-06-15T19:47:04Z
# Description: A curated list of awesome Python frameworks, libraries, 
# software and resources

# print("\nSelected info about 1st rep:")
# # print name of project
# print('Name:', repo_dict['name'])
# # entire dictionary represents project owner, so use key owner to access
# # dict representing owner and key login to get owner's login name
# print("Owner:", repo_dict['owner']['login'])
# # print how many stars owner has earned
# print('Stars:', repo_dict['stargazers_count'])
# # url for git repos
# print('Repository:', repo_dict['html_url'])
# # when was created
# print('created', repo_dict['created_at'])
# # when was updated
# print('updated:', repo_dict['updated_at'])
# # then description... these print statements already explanatory
# print('Description:', repo_dict['description'])

# # print num of keys in dict to see how much info we have
# print("\nKeys:", len(repo_dict))
# # now print out the dict keys to see info included
# for key in sorted(repo_dict.keys()):
#     print(key)

# # Process results.
# print(response_dict.keys())

# create 2 empty lists. We need name of each project to label bars
# and stars to ddetermine height of the bars
names, stars = [], []
# loop througha all dict in repo_dicts
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

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
chart.add('', stars)
chart.render_to_file('e07_python_repos.svg')