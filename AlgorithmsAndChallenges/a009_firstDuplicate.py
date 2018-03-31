'''
Note: Write a solution with O(n) time complexity and O(1) additional 
space complexity, since this is what you would be asked to do during a real interview.

Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal 
index. In other words, if there are more than 1 duplicated numbers, return the 
number for which the second occurrence has a smaller index than the second 
occurrence of the other number does. If there are no such elements, return -1.
'''

# Here's my solution
'''
When you want to store some values which you'll be iterating over, Python's list constructs 
are slightly faster. However, if you'll be storing (unique) values in order to 
check for their existence, then sets are significantly faster.

It turns out tuples perform in almost exactly the same way as lists, but they 
do use less memory by removing the ability to modify them after creation (immutable).

https://stackoverflow.com/questions/2831212/python-sets-vs-lists

'''
def firstDuplicate1(a):
    totalList = set()
    for x in a:
        if x not in totalList:
            totalList.add(x)
        else:
            return x
    return -1

# I could have done:
def firstDuplicate(a):
	someSet = set()
	for x in a:
		if x in someSet:
			return x
		someSet.add(x)
	return -1



# Here's someone take on the question
# This one made me think it out for a bit to understand why it's correct
def firstDuplicate3(a):
    for i in a:
        a[abs(i)-1] *= -1
        print("first is: " + str(a))
        if a[abs(i)-1] > 0:
            return abs(i)
    return -1

a = [2,4,3,3,5,2]

print("The answer is " + str(firstDuplicate3(a)))