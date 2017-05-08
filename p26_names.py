#NOTE when calling file names, make sure they don't start with numbers!
# otherwise try doing:
# __import__(25_testName) 

from p25_testName import get_formatted_name

print("Enter 'q' at any time to quit. ")
while True:
    first = input("\nfirst name please: ")
    if first == 'q':
        break
    last = input("\nlast name please: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")