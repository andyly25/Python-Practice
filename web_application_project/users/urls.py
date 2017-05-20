# define url patterns for users

from django.conf.urls import url
# we import the default login view
from django.contrib.auth.views import login

from . import views


urlpatterns = [
    # Login page
    # users tells Django to look in users/urls.py
    # login tells to send requests to Django default login view
    # NOTE: we aren't writing our own view function.
    # we pass a dictionary telling Django where to find template about to write
    # Will be part of users app, not leraning_logs app
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    # Logout page
    url(r'^logout/$', views.logout_view, name='logout')
    # registration page
    url(r'^register/$', views.register, name='register')
]