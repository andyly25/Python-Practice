# exercise from book

filename = 'text_files/learningPython.txt'
with open(filename) as fileobj:
    contents = fileobj.read()
    print("\n"+contents.rstrip())

print("\n REPEATING #2 **********************")

with open(filename) as fileobj:
    for line in fileobj:
        print("\n" + line.rstrip())


print("\n REPEATING #3 **********************")
fileList = ''
with open(filename) as fileobj:
    lines = fileobj.readlines()

for line in lines:
    newLine = line.replace('Python', 'JavaScript')
    fileList += newLine

print(fileList)