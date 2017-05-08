#importing regex
import re

# #simple greeting / modified :)
# def greet_user(username):
#     if(username == 'undefined'):
#         print("Aborting, no username was made")
#     else:
#         print("hello " + username.title())

#now you call the function to do some work
# username = input("Please enter your username ")
username = ""

while username != 'quit':
    username = input("Please enter your username with no Numbers" +\
        " or 'quit to escape' ")
    #using regex to check if does not match only letters
    if username == 'quit':
        username = 'undefined'
        break
    elif not re.match("^[a-zA-z]*$", username):
        continue
    else:
        break
    ##This would see if username is an int
    # try:
    #     val = float(username)
    # except ValueError:
    #     print("That's not an int!")

greet_user(username)


# #using multiple arguments
# def family(one, two, three):
#     print('The one bringing home the dough is: ' + one.title())
#     print('The one doing most of the chores is: ' + two.title())
#     print('The one studying is: ' + three.title())

# # #This is the simple way
# # count = 0
# # members = []
# # while count < 3:
# #     person = input("Enter your family name: total of 3 ")
# #     members.append(person)
# #     count +=1

# # family(members[0], members[1], members[2])

# members = input("Enter three members separated by commas: ")
# members_list = members.split(',')
# # print (members_list)
# family(members_list[0], members_list[1], members_list[2])


# #You can even use keyword arguments so order doesnt matter
# #atype = dog is the default if nothing is given
# #passing arguments soo fun
# def dog(atype, aname):
#     print("\nMy " + atype.lower() + " is called " + aname.title())

# dog('retriever', 'Barry')
# dog('Barry', 'retriever')
# dog(aname='phiLlis', atype='ChiHuahua' )


# def describe_pet(pet_name='Bob', animal_type = 'dog'):
#     print("\nI have a " + animal_type.lower())
#     print("It is called: " + pet_name.title())

# describe_pet(pet_name = 'wally')
# describe_pet('sue', 'alligator')
# describe_pet('daisy')
# describe_pet()


# #optional arguments
# def get_formatted_name(first, last, middle=''):
#     if middle:
#         fullname = first + ' ' + middle + ' ' + last
#     else:
#         fullname = first + ' ' + last
#     return fullname.title()

# musician = get_formatted_name('miley', 'cyrus')
# print (musician)
# ranJoe = get_formatted_name('joe', 'jill', 'james')
# print(ranJoe)

# #optional arguments
# def get_formatted_name(first, last, middle=''):
#     person = {'first': first, 'last': last}
#     if middle:
#         person['middle'] = middle
        
#     return person

# musician = get_formatted_name('miley', 'cyrus')
# print (musician)
# ranJoe = get_formatted_name('joe', 'jill', 'james')
# print(ranJoe)


# #Passing a list
# def greet_users(names):
#     for name in names:
#         print("hello " + name.title())

# username = ['bill', 'joe', 'margaret']
# greet_users(username)


# #accepting arbitrary number of args
# #the * makes an empty tuple called toppings
# #if you want multiple args, keep the arbitrary at end by default
# def make_icecream(size, *toppings):
#     print("\nMaking a "+ str(size)+ " scoop ice cream with the "  
#         "following toppings")
#     for topping in toppings:
#         print("- "+topping)

# make_icecream(2, 'banana')
# make_icecream(5, 'strawberry', 'oreos', 'gummies')


# #arbitrary keyword arguments
# # **keyword causes python to create an empty dictionary and pack
# # name-key values into it

# def built_profile(first, last, **info):
#     profile = {}
#     profile['first_name'] = first.title()
#     profile['last_name'] = last.title()
#     for key, value in info.items():
#         profile[key]=value.title()
#     return profile

# user_profile = built_profile('jake', 'johnson', location = 'harvard',
#                             field='mathematics')

# print(user_profile)


# #importing functions from other files
# # import icream #would import all functions of that file
# # below would import a specific one
# # importing more than one specific is from blah import blah, blah2
# # you can make an alias using 'as'
# from icecream import make_icecream as mi

# mi(5, "bananan")
# mi(10, 'chocolate', 'gummis', 'strawberries')


# #You can even use alias for a modulo
# import icecream as i
# i.make_icecream(5, 'strawberry', 'oreos')


# # you can import all functions using
# # from icecream import *



