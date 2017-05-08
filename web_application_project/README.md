# Learning Log

## Details
- allows users to make journal entries as they learn about each topic.ls
- home page should describe the site and invite user to register or login.
- if logged in, can create new topics, add new entries, and edit.

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