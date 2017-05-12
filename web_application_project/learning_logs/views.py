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