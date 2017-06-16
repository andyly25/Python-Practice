# let's clean up the file more
import requests
import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

def get_response():
    # make api call and return a response
    url = ('https://api.github.com/search/'
        'repositories?q=language:java&sort=stars')
    r = requests.get(url)
    return r

def get_repo_dicts(response):
    # return set of dicts representing pop repos
    response_dict = response.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def get_names_plot_dicts(repo_dicts):
    # process set of repo dicts, and pull data for plot
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        # specify a label if no description
        description = repo_dict['description']
        if not description:
            description = "No description provided."

        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': description,
            'xlink': repo_dict['html_url'],
        }

        plot_dicts.append(plot_dict)

    return names, plot_dicts

def make_visualization(names, plot_dicts):
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
    chart.title = 'Most starred Java Projects on GitHUb'
    chart.x_labels = names

    # since we don't need this data series to be labeled we pass empty string
    chart.add('', plot_dicts)
    chart.render_to_file('e07_java_repos.svg')

r = get_response()
repo_dicts = get_repo_dicts(r)
names, plot_dicts = get_names_plot_dicts(repo_dicts)
make_visualization(names, plot_dicts)