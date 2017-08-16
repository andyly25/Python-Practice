'''
    Tail Recursion: when the recursive call is the very last thing in the 
    function. Function that does nothing after recursing.
    - You can pass result of recursive call through directly instead of waiting
        - no stack space consumed.
    
    Any tail recursion can be reimplemented nonrecursively by enclosing the 
    body in a loop for repetition and replacing recursive call with new params 
    by reassigning existing params to the values. 

    NOTE: if you want to do binary search with Strings, make sure to have list 
    sorted first, I tried without doing so and errors popped up
'''

# Non recursive implementation of binary search
# return true if target found in python list
def binarySearchIterative(data, target):
    low = 0
    high = len(data)-1
    while low <= high:
        # grab the midpoint
        mid = (low+high)//2
        # we have found a match!
        if target == data[mid]:
            print("I have found the holy g... erm " + str(target))
            return True
        # looks at values left of mid
        elif target < data[mid]:
            high = mid-1
        # looks at values right of mid
        else:
            low = mid + 1
    print("failure... and they were never seen again")
    return False

test = [0,1,2,8,12,18,268,928]
binarySearchIterative(test, 928)

# I googled how someone else did it and it was very similar to textbook
def binarySearch(list, item):
    first = 0;
    last = len(list)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint +1
    return found

testlist = [0,1,2,8,12,18,268,928]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 268))


# reverse elements in sequence S
def reverseIterative(S):
    start, stop = 0, len(S)
    while start < stop -1:
        # swap first and last
        S[start], S[stop-1] = S[stop-1], S[start]
        # narrow the range
        start, stop = start + 1, stop - 1
    return S


reversalList = [1,2,3,4,5,6,7,8]
print(reverseIterative(reversalList))