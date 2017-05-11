# imports the render() function which renders the response based on data
# provided by views.
from django.shortcuts import render

# Create your views here.

'''
if URl request matches the pattern, Django searches  for function called 
index() in the views.py and then passes in a request.
'''

# Home page for learning log
def index(request):
    # render uses two args: original request object and a template to build
    return render(request, 'learning_logs/index.html')