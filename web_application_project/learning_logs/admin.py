from django.contrib import admin

#registering Topic, Entry with admin site
from learning_logs.models import Topic, Entry

# Register your models here.
# tells Django to manage the model through admin site
admin.site.register(Topic)
admin.site.register(Entry)

