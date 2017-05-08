# Exception practice!

# # try sees if it can run the code, if not, goes to except block and see if
# # error matches on raised and runs code in that block
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you can't divide by 0!")


# # preventing crashes 
# print("Give me two numbers and I'll divide them.")
# print("Enter 'q' to quit. ")

# while True:
#     first_num = input('\nfirst number: ')
#     if(first_num == 'q'):
#         break
#     second_num = input('\nsecond number: ')
#     if second_num == 'q':
#         break
#     try:
#         answer = int(first_num)/int(second_num)
#     except ZeroDivisionError:
#         print("Can't divide by 0")
#     except ValueError:
#         print("\nERROR: Please use numbers, NOT letters")
#         continue
#     else:
#         print(answer)


# file exception error
# UnicodeEncodeError is a huge pain in the ###

# def count_words(filename):
#     try:
#         # with open(filename, encoding="ascii", errors="surrogateescape") as f_obj:
#         with open(filename, encoding="utf-8") as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError as e:
#         msg = "Sorry, the file " + filename + " does not exist."
#         print(msg)
#     else:
#         # Count the approximate number of words in the file.
#         words = contents.split()
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) + 
#             " words.")

# filename = 'text_files/alice.txt'
# filenames = ['text_files/alice.txt', 'siddharta.txt', 
# 'text_files/moby_dick.txt']
# for filename in filenames:
#     count_words(filename)


# Failing silently
# you would use 'pass' in the except block and continue on with program

def count_words(filename):
    try:
        # with open(filename, encoding="ascii", errors="surrogateescape") as f_obj:
        with open(filename, encoding="utf-8") as f_obj:
            contents = f_obj.read()

    except FileNotFoundError as e:
        pass
    else:
        # Count the approximate number of words in the file.
        
        words = contents.split()
        num_words = len(words)
        print("\nThe file " + filename + " has about " + str(num_words) + 
            " words.")

def theCount(filename):
    thecount = 0
    try:
        # with open(filename, encoding="ascii", errors="surrogateescape") as f_obj:
        with open(filename, encoding="utf-8") as f_obj:
            lines = f_obj.readlines()

    except FileNotFoundError as e:
        pass
    else:
        # Count the approximate number of words in the file.
        for line in lines:
            thecount += line.lower().count('the')
        print("\n'the' appeared: " + str(thecount) + " times.")

filename = 'text_files/alice.txt'
filenames = ['text_files/alice.txt', 'siddharta.txt', 
'text_files/moby_dick.txt']
for filename in filenames:
    count_words(filename)
theCount(filename)


