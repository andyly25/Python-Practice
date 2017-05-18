# imports the render() function which renders the response based on data
# provided by views.
from django.shortcuts import render
# This import redirects reader back to topics page after submitting topic
from django.http import HttpResponseRedirect
# the reverse() function determine URL from named URL pattern:
# Django will generate the URL when page requested
from django.core.urlresolvers import reverse


# import model associated with date we need
from .models import Topic, Entry
# import the form we need
from .forms import TopicForm, EntryForm

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
'''
    This function takes in a request as a parameter.
    When a user sends a request for this page, the browser will send
    a GET request. After filling out the form, a POST request will be sent.
    We'll know if user requesting a blank form (GET) or ask to process 
    completed form (POST)
'''
# Add a new topic
def new_topic(request):
    # Determines whether request is GET or POST
    if request.method != 'POST':
        # no data submitted; create blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        # create an instance of TopicForm and pass data entered by user, which 
        # is the request.POST
        form = TopicForm(request.POST)
        # can't save submitted form until verified that data is valid.
        # All field in form required by default and data must match 
        # field types expected.
        if form.is_valid():
            # if valid, writes data from form to database
            form.save()
            # once data is saved, we use reverse to get URL for topics page 
            # and pass URL to HttpResponseRedirect(), redirecting to topics
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    # send the form to the template in a context dictionary
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

# Add new entry for particular topic
def new_entry(request, topic_id):
    # we need to grab topic_id so that we get the correct topic to render
    topic = Topic.objects.get(id=topic_id)
    # check if request is POST or GET
    if request.method !='POST':
        # no data, create blnak form
        form = EntryForm()
    else:
        # Post data submitted; process data
        form = EntryForm(data=request.POST)
        # check if form is valid
        if form.is_valid():
            # commit=False is to tell Django to create new entry object and 
            # store in new_entry w/o save to db yet
            new_entry = form.save(commit=False)
            # we set the new_entry's topic that was pulled at beginning
            new_entry.topic = topic
            # now we save entry to db with correct associated topic
            new_entry.save()
            # redirect user to topic page they made an entry for
            return HttpResponseRedirect(reverse('learning_logs:topic', 
                                                args=[topic_id]))
            
    context = {'topic':topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

# edit an existing entry
# when the page receives a GET request, edit_entry() returns a form for edit.
# When receives a POST request with revision, saves into the db
def edit_entry(request, entry_id):
    # Using entry_id to get entry object we want and edit topic associated
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request != 'POST':
        # GET: initial request, pre-fill forms with current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process
        # the two args tells Django to create a form instance based on info 
        # associated with existing entry object and updated from request.POST
        form = EntryForm(instance=entry, data= request.POST)
        if form.is_valid():
            # if valid, can save with no args
            form.save()
            # redirect to topic page with updated page
            return HttpResponseRedirect(reverse('learning_logs:topic', 
                args=[topic_id]))

    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)