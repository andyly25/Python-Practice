#simple dictionary
##feel free to comment out parts and test
##dictionaries are key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
#you can add in more elements like this
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)
#changing value similar to arrays
alien_0['color'] = 'yellow'
print(alien_0)

#tracking movement
alien_0['speed'] = 'medium'
print('Original x_pos: ' + str(alien_0['x_pos']))

if(alien_0['speed'] == 'slow'):
    x_increment = 1
elif(alien_0['speed'] == 'medium'):
    x_increment = 2
else:
    x_increment = 3

alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print("new x_pos is: " + str(alien_0['x_pos']))

#you can use del to remove a key value pair
del alien_0['points']
print(alien_0)

favorite_language = {
    'bob': 'python',
    'bill': 'java',
    'sam': 'c',
    'bobby': 'python',
    'sammy': 'ruby'
}

print("Sammy's favorite language is: " + favorite_language['sammy'])

#looping through both key and values
for key, value in favorite_language.items():
    print("\nKey: "+ key)
    print("Value: "+ value)
    print(key.title() + "'s favorite language is: " + value.title())

#looping through just the key
for names in favorite_language.keys():
    print(names)
#this works just the same by default
#for name in favorite_language:

bff = ['bill', 'sammy']
for name in favorite_language.keys():
    print(name.title())

    if name in bff:
        print(" Hi! " +name.title() + " I see you like " + favorite_language[name].title() + ".")
    else:
        print("Hi " + name.title())

if 'erin' not in favorite_language.keys():
    print("please take our poll Erin!")

#if you want to sort the dictionary, wrap around the with sorted
for name in sorted(favorite_language.keys(), reverse = True):
    print("THanks for taking the poll " + name.title())

#for just the values
for language in favorite_language.values():
    print(language.title())

#to get rid of repeats you use set()
print("\n non repeated language")
for language in set(favorite_language.values()):
    print(language)

#nesting, in this case let's make a list of dictionaries
alien_1 = {'color': 'green', 'points': 5}
alien_2 = {'color': 'yellow', 'points': 10}
alien_3 = {'color': 'red', 'points': 15}

aliens = [alien_1, alien_2, alien_3]

for alien in aliens:
    print(alien)

#now let's make a lot of enemies
enemies = []
#making 30 of them
for enemy_number in range(30):
    new_enemy = {'color': 'green', 'points': 5, 'speed': 'slow'}
    enemies.append(new_enemy)

#let's modify some of the aliens
for enemy in enemies[0:3]:
    if enemy['color'] == 'green':
        enemy['color'] = 'purple'
        enemy['speed'] = 'medium'
        enemy['points'] = 10
    elif enemy['color'] == 'purple':
        enemy['color'] = 'red'
        enemy['speed'] = 'hard'
        enemy['points'] = 15

#show the first 5 enemies
for enemy in enemies[:5]:
    print(enemy)

#show how many aliens were made
print("total number of aliens is: " + str(len(enemies)))



#list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust']+ "-crust pizza " + 
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#using another for loop inside

favorite_language2 = {
    'bob': ['python', 'scala'],
    'bill': ['java'],
    'sam': ['c', 'swift'],
    'bobby': ['python'],
    'sammy': ['ruby', 'php']
}

for name, languages in favorite_language2.items():
    print("\n" + name.title() + "'s favorite language(s) are: ")
    for language in languages:
        print("\t" + language.title())

###A dictionary in a dictionary
users = {
    'wwilly': {
        'first': 'wally',
        'last': 'willy',
        'location': 'harvard'
    },
    'ckatie':{
        'first': 'cynthia',
        'last': 'katie',
        'location': 'mission'
    }
}

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print('Full name: ' + full_name)
    print('Location: ' + location)


#a bit of practice
acquaintences = {
    'joe': [25, 33, 10],
    'jim': [42, 94, 19, 20],
    'joey': [52, 18, 83],
    'jimmy': [73, 82]
}

for acquaintence, numbers in acquaintences.items():
    print("\n" + acquaintence.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("\t" + str(number))