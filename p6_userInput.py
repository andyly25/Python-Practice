#note uncomment whichever code you want to test
#you can use (command + /) or (control + /) after selected block of code

##parroting / mirror
# parrot = input("Tell me something and I'll repeat back to you: ")
# print(parrot)


## Another practice
# prompt = "I'd like to know your name for identification purposes. "
# prompt += "\nWhat is your first name?"

# name = input(prompt)
# print("\nHello, " + name + "!")


# #input() takes everything as a string, so lets use ints
# height = input("How tall are you, in feet? ")
# height = int(height)

# if height >= 5:
#     print("You're tall enough to ride!")
# else:
#     print("Come back again when you're taller.")


# #You can use modulo operator ('%') to determine odd or even 
# num = input("Enter a number and I'll say if odd or even ")
# num = int(num)

# if(num%2 == 0):
#     print(str(num) + " is even!")
# else: 
#     print(str(num) + ' is odd!')

### NOTE, when using these inputs, you should have checks to see 
### if user input matches the type you want! COMING UP!


# #WHILE LOOP 
# curr_num = 1
# while curr_num <=5 :
#     print(curr_num)
#     curr_num += 1


# #unending loop, until condition met
# message = "\nEnter something, it will be mirrored "
# message += "\nEnter 'quit' to stop the program "
# parrot = ""
# while parrot != "quit":
#     parrot = input(message)

#     if parrot != 'quit':
#         print("\n" + parrot)


# #now let's use a FLAG: True and False
# message = "\nEnter something, it will be mirrored "
# message += "\nEnter 'quit' to stop the program "
# active = True
# while active:
#     parrot = input(message)

#     if parrot == 'quit' :
#         active = False
#     else:
#         print(parrot)


# #Now let's try using 'break',it stops the loop and continues elsewhere
# message = "\nEnter something, it will be mirrored "
# message += "\nEnter 'quit' to stop the program "
# active = True
# while active:
#     parrot = input(message)

#     if parrot == 'quit' :
#         break
#     else:
#         print(parrot + " active not changed so...IMPOSSIBLE TO LEAVE")

# print("FREEDOM")


# # Now we use 'continue to continue the loop'
# # This example the continue ignores the evens and only prints odds
# curr_num = 0
# while curr_num < 10:
#     curr_num += 1
#     if curr_num %2 == 0:
#         continue
#     print (curr_num)


### NOTE: CAREFUL OF INFINITE LOOP, TEST ALL WHILE LOOPS


# #Move items from one list to another
# #start: users needed to be verified
# #then empty list to hold confirmed

# unconfirmed_users = ['jake', 'josh', 'jan']
# confirmed_users = []

# #now verifiy until no more unconfirmed
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)

# #display confirmed user
# print('\n following users confirmed: ')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())



# #Let's say we want to remove all instances of a word from list
# colors = ['red', 'blue', 'pink', 'red', 'purple', 'blue', 'red']
# print(colors)

# while 'red' in colors:
#     colors.remove('red')

# print(colors)


##challenge, try to remove all duplicates
## hint, you make a new list to populate and check to see if not already
## in the list and append into new list

# colors = ['red', 'blue', 'pink', 'red', 'purple', 'blue', 'red']
# colorsN = []
# print(colors)

# for color in colors:
#     if color not in colorsN:
#         colorsN.append(color)

# print(colorsN)



#Filling a dictionary with user input
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What is your favorite sport? ")

    #store response into dictionary
    responses[name] = response

    #ask if more to take poll
    repeat = input("Let another respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#show results
print("\n----- Poll Results -----")
for name, response in responses.items():
    print(name + " likes " + response)