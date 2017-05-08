from collections import OrderedDict

#This allows us to always get responses in order they were added
favorite_languages = OrderedDict()

favorite_languages['bob'] = 'python'
favorite_languages['bill'] = 'c'
favorite_languages['sarah'] = 'ruby'
favorite_languages['chris'] = 'python'
favorite_languages['mall'] = 'java'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is: " + language.title())


