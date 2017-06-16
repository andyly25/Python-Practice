# goal: make an API that returns the IDs if current top articles on Hacker News

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from operator import itemgetter

# make an API call and store response.
# woops.. forgot the s in http and program wouldn't run
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
# print status of response
print("Status code:", r.status_code)

# This API call returns a list containing IDs of 500 most popular articles
# process info about each submission
submission_ids = r.json()
# set up empty list to store dictionaries
submission_dicts = []
# loop through IDs of top 30
for submission_id in submission_ids[:30]:
    #make separate api call for each by generating a URL that includes
    #current value of submission_id
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
        str(submission_id) + '.json')
    submission_r = requests.get(url)
    # print status of each request to see if successful
    print(submission_r.status_code)
    response_dict = submission_r.json()

    '''
    create a dictionary for submission being processed
    We store num of comments in dictionaries, if no comments, descendants 
    aren't present. If you're unsure if a key exists use dict.get(),
    which returns value associated with given key if it exists or value 
    provided doesn't exist.
    '''
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

# to sort list of dictionaries by # of comments we use itemgetter().
# 'comments' is the key and it uses the values stored to sort in reverse 
submission_dicts = sorted(submission_dicts, key = itemgetter('comments'),
                            reverse=True)

titles, plot_dicts = [], []
# once sorted, loop and print out three info: title, link, # comments
for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("comments:", submission_dict['comments'])
    titles.append(submission_dict['title'])
    plot_dict = {
        'value': submission_dict['comments'],
        'label': submission_dict['title'],
        'xlink': submission_dict['link']
    }
    plot_dicts.append(plot_dict)

# styling
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
my_config.y_title = "# of comments"

chart = pygal.Bar(my_config, style=my_style)
chart.title = "most active discussions on Hacker News"
chart.x_labels = titles

chart.add('', plot_dicts)
chart.render_to_file('e08_discussions.svg')
