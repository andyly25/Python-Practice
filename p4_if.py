colors = ['red', 'blue', 'purple', 'orange', 'yellow', 'green']
for color in colors:
    if(color == 'orange'):
        print(color.upper())
    elif (color != 'green'):
        print(color.title())
    else: 
        print("that's AK's favorite color "+ color)

#if case doesn't matter just use .lower() to compare

#using and to check multiple conditions (not &&)
age1 = 18
age2 = 21
age3 = 50

if(age1 >= 18 and age2<30):
    print("you're a young adult!")
if(age3 <18 or age3>31):
    print("you're not of the right age :(!")

chores = ['clothes', 'dishes', 'vacuum', 'sweeping', 'cooking']
hatedChore = 'teaching'
if hatedChore not in chores:
    print(hatedChore.title() + ", who wants to do this?!")

#This statement checks if the list is empty first 
if chores:
    for chore in chores:
        if(chore == 'dishes'):
            print("Don't want to do "+chore)
        elif(chore != 'cooking'):
            print("Sure, I'll do the " + chore)
        else:
            print("Time to cause mayhem with my "+ chore)
else:
    print("guess i can be lazy today")

groceryList = ['paper', 'food', 'computer', 'videogames', 'bread', 'fruits']
pickedUp = ['paper','chips', 'food', 'fruits', 'fish']

for item in pickedUp:
    if item in groceryList:
        print('Yup, I picked up the '+item)
    else:
        print('Sorry, the grocery didnt have this item: '+item)
