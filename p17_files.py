# READING FILES

# # We first open the file we want read
# # argument needed is the name of the file
# # 'with' closes the file once access no longer needed
# # you can use close() but bugs can cause file to stay open and errors occurs
# # only difference is that extra blank line since read returns empty string
# # use rstrip() to remove after read
# with open('text_files/pi_digits.txt') as file_object:
#     # note in windows you use a backslash instead
#     # you can use absolute paths and store into variables, for now folder
#     contents = file_object.read()
#     print(contents.rstrip())


# # Reading line by line
# filename = 'text_files/pi_digits.txt'
# with open (filename) as file_object:
#     for line in file_object:
#         #problem is a new blank line printed everytime, use rstrip()
#         print(line.rstrip())


# # Making a list of lines from a file
# filename = 'text_files/pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())


# # Working with file's contents
# filename = 'text_files/pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))


# # Large files
# filename = 'text_files/pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(pi_string[:52] + ". . .")
# print(len(pi_string))



# Writing to a file
# 'w' opens file into write mode
# 'r' reads file, 'r+' is read and write, 'a' is append
# python can only write strings to a text file
# to store numbers, convert data to str() first
filename = 'text_files/blarg.txt'
with open(filename, 'w') as file_object:
    #add new lines \n if you want to be on different lines
    file_object.write("Programming sure is tiring.\n")
    file_object.write("Sleepy as always.\n")

with open(filename, 'a') as file_object:
    file_object.write("Appending this into the file~\n")



# exercise
count = 0
guestList = []
response = ''
filename = 'text_files/guest.txt'
while response != 'quit':
    
    response = input("\nHello guest, what is your name?" +
        "\nType 'quit' to leave. : ")
    if response != 'quit':
        count += 1
        print("\nHello " + response + "!")
        with open(filename, 'a') as file_object:
            file_object.write("#" + str(count) + " " + response + "checked in."+
                "\n")
        #I don't need a list if directly into a file
        guestList.append(response)

with open(filename, 'r') as file_object:
    lines = file_object.readlines()

for line in lines:
    print("\n" + line.rstrip())






