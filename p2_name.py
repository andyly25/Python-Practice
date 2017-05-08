name = "bob schnieder"
#title() displays each word in title case
print (name.title())
print(name.upper())
#lower() lowercases all words, useful for storing data
print(name.lower())
#concatenating strings together
first_name = "biLl"
last_name = "StanLey"
full_name = (first_name + " " + last_name).title()
statement = "Hello" + " "+ full_name.title()
print(statement)
#adding a tab is \t, newlines is \n
print ("\tBlah\ntoo bright")
#now to strip whitespace you use both lstrip() and rstrip(), or strip() for both
sample = "   zzzsleepy  "
ssample = sample.strip()
print (ssample)
aposTest = full_name+' once said "Better to do something you like, than to live'+ \
' life miserably"'
print(aposTest)
#usage of numbers
age = 23
print("Happy " + str(age) +"rd birthday!")
print(3/2)