from django.db import models
""" 
A model, aka just like a class, tells Django how to work with the data.
It has attributes and methods. 
"""

# Create your models here.
# Created class called Topic which inherits from Model
#   Model defines basic functionality of a model
#   in this case we are using charField and DateTimeField
class Topic(models.Model):
    # A topic user is learning about
    
    # CharField is used to store a small amount of text.
    # We then tell Django how much space to reserve in the database
    text = models.CharField(max_length=200)
    # DateTimeField records date and time data
    # auto_now_add adds the current date and time and we store it
    date_added = models.DateTimeField(auto_now_add=True)

    # We need to tell Django which attribute to use by default when it 
    # displays info about a topic. This will return a string stored in
    # the text attribute.
    def __str__(self):
        # return string representation of model
        return self.text

class Entry(models.Model):
    # learned from topic

    # topic is a foreign key: reference to another record on db.
    # So each topic is assigned key or id when created and we can use this to 
    # retrieve all the entries associated with that topic.
    topic = models.ForeignKey(Topic)
    # no size-limit for individual entries and then adding a timestamp
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Meta holds extra info for managing a model:
    #   Using entries when more than one entry
    #   otherwise Django calls it Entrys
    class Meta:
        verbose_name_plural = 'entries'

    # Tells Django which info to show when refer to individ. entries
    # we're just looking at 50 characters since it could be large body of text.
    def __str__(self):
        # return a string representation of model
        return self.text[:50] + "..."