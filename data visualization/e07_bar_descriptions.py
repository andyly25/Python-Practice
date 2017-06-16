import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
# have to add this line to be able to render tooltips correctly
chart.force_uri_protocol = 'http'

chart.title = 'Python Projects'
chart.x_labels = ['awesome python', 'httpie', 'thefuck']

# define a list that contains 3 dictionaries of the current top repos
# Each dict has 2 keys: value and label; value for how tall, label for tooltip
plot_dicts = [
    {'value': 35030, 'label': 'Descripton of awesome python.'},
    {'value': 30066, 'label': 'Description of httpie.'},
    {'value': 28451, 'label': 'Description of thefuck.'},
]

# pass in the list of dicts representing the bars
chart.add('', plot_dicts)
chart.render_to_file('e07_bar_descriptions.svg')