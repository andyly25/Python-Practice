from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# imported necessary form functions
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# log the user out
def logout_view(request):
    # we call logout() which uses request obj as arg
    logout(request)
    # redirect to homepage
    return HttpResponseRedirect(reverse('learning_logs:index'))

# register a new user
def register(request):
    # check if responding to GET request
    if request.method != 'POST':
        # display blank registration form
        form = UserCreationForm()
    # if POST, make instance of UserCreationForm with submitted data
    else:  
        # process completed form
        form = UserCreationForm(data=request.POST)

        # check if data is valid
        if form.is_valid():
            # if valid and nothing malicious found, save new created object 
            new_user = form.save()
            # login user and redirect home page
            # since password is already validated, we store data into auth_usr
            # and using that info to login
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password'])
            # login creating a valid session for new user
            login(request, authenticated_user)
            # redirect user to home page
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {form:'form'}
    return render(request, 'users/register.html', context)