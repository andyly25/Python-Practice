# Define URL patterns for learning_logs
# Import the url function which is used for mapping URLs to views
from django.conf.urls import url

# Also import views module where the dot ('.') tells python to import views
# from the same directory as the current urls.py module
from . import views

# urlpatterns here is the list of individual pages that can be requested 
# from the learning_logs app

'''
    a call to the url function that takes three args.

    Regular expressions called regexes... you studied this before so, make 
    sure to review up on it, really useful.

    first is the regular expression which Django use to find a match.
    let's analyze the r'^$'
        r           : tells python to interpret as rawstring
        ' ' (quotes): tells where the regular expression begins and ends
        ^ (caret)   : tells python to find beginning of string
        $ (dollar)  : tells python to look for end of string
    Overall it tells python to ignore the base URL for project which is:
    http://localhost:8000/

    the second argument tells what view view function to call.
    So if a match is found, view.index will be called.

    the third argument provides the name index represent this URL pattern,
    can be used in other sections of code.

'''
urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all topics
    # This pattern will match any URL with the base URL followed by topics
    url(r'^topics/$', views.topics, name='topics'),
    # Single topic page
    # /(?P<topic_id>\d+)/ matches integer between two forward slashes
    # and stores integer value into arg topic_id.
    # The parenthesis captures value stored in the URL.
    # \d+ matches any number of digits that appear between forward slashes
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # page for adding new topic
    # This will send requests to the view function new_topic()
    url(r'^new_topic/$', views.new_topic, name='new_topic')
]