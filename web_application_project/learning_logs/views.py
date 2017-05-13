# imports the render() function which renders the response based on data
# provided by views.
from django.shortcuts import render

# import model associated wit date we need
from .models import Topic

# Create your views here.

'''
if URl request matches the pattern, Django searches  for function called 
index() in the views.py and then passes in a request.
'''

# Home page for learning log
def index(request):
    # render uses two args: original request object and a template to build
    return render(request, 'learning_logs/index.html')


# Showing all topics 
# onle needs one parameter: request Django received from server
def topics(request):
    # query the db by sorting Topic obects by date_added and store in topics
    topics = Topic.objects.order_by('date_added')

    # define a context to send to template.
    # context is a dictionaty in which keys are are names used to access data
    # and values are data needed to be sent to template.
    context = {'topics': topics}

    # We pass context to render, request object, and path to build the page
    return render(request, 'learning_logs/topics.html', context)

# show a single topic and all its entries
# /(?P<topic_id>\d+)/ value is used for the topic_id argument.
def topic(request, topic_id):
    # get used similar to the Django shell to retrieve topic
    # note this is a query; queries db for specific info
    topic = Topic.objects.get(id=topic_id)
    # have ordered by date_added, '-' sign means reverse order
    # note this is a query
    entries = topic.entry_set.order_by('-date_added')
    # store topic and entries in the context dicitonary
    context = {'topic':topic, 'entries': entries}
    # finally send context to topic.html
    return render(request, 'learning_logs/topic.html', context)