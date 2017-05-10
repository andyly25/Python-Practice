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
    - dot at end creates new project with directory structure
    - created a *manage.py*: takes in commands and feeds them to relevant parts of Django to run
    - 3 files within folder created: settings.py, urls.py, wsgi.py
        - settings: how Django interacts with the system and manages the project
        - urls: tell which pages to build in response to browser requests
        - wsgi: helps Django serve the files it creates
            - acronym for: web server gatewat interfaces
- **Creating the database**
    - python manage.py migrate
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

### Django Shell
- you can use the Django shell for testing and troubleshooting the data
    - **python manage.py shell**
    - e.g. **from learning_logs.models import Topic**
    - e.g. **Topic.objects.all()**
    - this imports our model Topic and then we get all instances of the model with the list being returned called a *queryset*