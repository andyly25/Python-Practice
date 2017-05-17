## Table of Contents
1. [Learning Log](#learning-log)
2. [Details](#details)
3. [Setting-up](#note-on-setting-up)
4. [Django Admin](#django-admin)
5. [Define Model](#defining-the-entry-model)
6. [Django Shell](#django-shell)
7. [Making Pages](#making-pages)
    - [Mapping a URL](#mapping-a-url)
    - [Writing a View](#writing-a-view)
8. [User Accounts](#user-accounts)

# Learning Log 

## Details
- allows users to make journal entries as they learn about each topic.ls
- home page should describe the site and invite user to register or login.
- if logged in, can create new topics, add new entries, and edit.
- Tutorial from *Python Crash Course*

### Note on setting up:
- Using a virtual environment to work with Django
    - a venv is place where you can install packages and isolate from all other Python packages
- creating my venv: **conda create -n ll_env python=3.5.2 anaconda**
    - activate by: **source activate ll_env**
    - deactivate by: **source deactivate ll_env**
- inside my venv: **pip install Django**
- creating a project: **django-admin.py startproject learning_log .**
    - **IMPORTANT: dot** at end creates new project with directory structure
    - created a *manage.py*: takes in commands and feeds them to relevant parts of Django to run
    - 3 files within folder created: settings.py, urls.py, wsgi.py
        - settings: how Django interacts with the system and manages the project
        - urls: tell which pages to build in response to browser requests
        - wsgi: helps Django serve the files it creates
            - acronym for: web server gatewat interfaces
- **Creating the database**
    - **python manage.py migrate**
    - migrating the database === modifying database
        - first time is to make sure db matches current state of project
        - it creates database tables to store info used (Synchronize unmigrated apps) and make sure db struct matches current code (Apply all migrations)
        - created a db.sqlite3 
- Viewing the project
    - in terminal type in: **python manage.py runserver**
    - This starts a server so you can view the project
        - http://127.0.0.1:8000/ or http://localhost:8000/
- **Starting an App**
    - **python manage.py startapp learning_logs**
    - creates infrastructure to build an app
    - created models, admin, and views python files
        - Recall the MVC model 
    - after adding learning_logs to settings.py, modify database
        - **python manage.py makemigrations learning_logs**
        - makemigrations: tells Django to figure out how to modify db to match new model defined
        - also created a migration file that creates table for Topic
    - apply migration
        - **python manage.py migrate**
- Modifying data in **3 easy steps**:
    - modify models.py -> makemigrations on project -> migrate project

### Django Admin
- setting up a superuser: creating a user with all privileges on site
    - **python manage.py createsuperuser**
    - prompts for username, e-mail, then password
    - Note: Django stores a string derived from the password with HASH. Hashes your entry and compare it to stored hash.
- now after registering Topic in admin you can access admin site
    - http://localhost:8000/admin/

### Defining the Entry model
- need to define a model for different kinds of entries users would make; where each entry associated to a particular topic.
    - this is a many to one relationship
    - so update model to include Entry then...
    - follow the 3 easy steps and then register in admin.py
        - hint... models -> makemigrations -> migrate

### Django Shell
- you can use the Django shell for testing and troubleshooting the data
    - **python manage.py shell**
    - e.g.1 **from learning_logs.models import Topic**
    - e.g.1 **Topic.objects.all()**
    - this imports our model Topic and then we get all instances of the model with the list being returned called a *queryset*
    - e.g.2 **topics = Topic.objects.all()**
    - e.g.2 **for topic in topics:**
    - e.g.2     **print(topic.id, topic)**
        - store the queryset in topics then print each topic's id attribute and string representation
    - e.g.3 **t = topic.objects.get(id=2)**
    - e.g.3 **t.text**
    - e.g.3 **t.date_added**
    - e.e.3 **t.entry_set.all()**
        - knowing the id from previous example, we can then use the id to get more info about attributes associated with the id.
        - to get data from foreign key relationship, use lowercase of related model with _set
- Note: Restart shell session everytime you modify the models to see the newest changes

## Reference: https://docs.djangoproject.com/en/1.8/topics/db/queries/

### Making Pages
- web pages consists of 3 stages in Django:
    1. defining URLs
        - Describes to Django what to look for when matching browser request with a site URL
    2. writing views
        - Each URL matches to a particular view; view retrieves and processes required data to run the page.
    3. writing templates 
        - the view then calls a template which builds a page that a browser can read.

#### Mapping a URL
- edit urls.py in **learning_log**
- added in learning_logs.urls into the urlpatterns
- Now to make a second urls.py in the **learning_logs** folder
- Note, a lot of comments in each file on what each thing does

#### Writing a View
- We go edit the **views.py** within the learning_logs directory
- Now to write a template so create a **templates** folder in learning_logs
    - within templates make a **learning_logs** folder
    - this sets a structure so that Django can interpret unambiguously
        - we create an index.html within the folder
- Template Inheritence:
    - To do so we make a base.html that contains elements common to all pages.
    - include blocks so that everything that aren't inheriting from parent can go here, making each page unique. 
    - remember to use **{% extends (something) %}** at the beginning of child templates so Django knows what to look for. 
- Now that you know this... follow the [Making Pages](#making-pages) steps.
- Remember to update base.py if to include link to new pages

### User Accounts
- Want to allow users to add, edit, and delete their posts without going into admin.
- Adding form based page works in 3 easy steps + a new module:
    - Define a URL, write a view function, and write a template
    - addition of forms.py containing the forms
        - should be in same folder as models.py
- Requests:
    - GET: requests for pages that only read data from server
    - POST: when user needs to submit info through a form
        - we'll use POST method to process all our forms