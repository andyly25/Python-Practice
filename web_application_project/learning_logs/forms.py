'''
    form: any page that lets users enter and submit info.
    There is a need to validate the forms if the right data is being entered.
    Then after confirming that the data is not malicious we process and store 
    the data into the database.

    ModelForm uses info from the models to auto build the forms.

'''

# first import the forms module and model work with
from django import forms
from .models import Topic, Entry

# define a class which inherits from forms.ModelForm
# This is the simplest using a nested Meta class tell Django
# which model to base the form on and which fields to include.
class TopicForm(forms.ModelForm):
    class Meta:
        # we build a form from the Topic model 
        model = Topic
        # and include only the text field
        fields = ['text']
        # tells Django not to generate a label for textfield
        labels = {'text': ''}

# Adding another form associated with Entry model
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        # giving a blank label again
        labels = {'text': ''}
        # widget is HTML form elemnt
        # e.g. single/multi line textbox/area, or dropdown list
        # widgets overrides Django default widget choices
        # customize field text to be 80 col wide instead default 40
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
    