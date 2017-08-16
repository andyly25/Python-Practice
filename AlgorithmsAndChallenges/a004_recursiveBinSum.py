''' 
    binary recursion: when a fn makes two recursive calls.
    Summing of one or zero elements is trivial. Two or more can compute 
    sum of first half and sum of second half and add the two together.
    Let S be a sequence of numbers and there be n elements
'''

# return sum of num in slice S[start, stop]
def binarySum(S, start, stop):
    # if zero elements in the slice
    if start>=stop:
        return 0
    # if there is one element in slice
    elif start == stop-1:
        return S[start]
    # if there are >=2 in slice
    else:
        mid = (start + stop)
        return binarySum(S, start, mid) + binarySum(S, mid, stop)

'''
Analysis of the function above:
    consider n as a power of 2 using example binarySum(0,8)
    Size of range divided in half at each recursive call and so the depth
    of each recursion is 1+log2n.

    therefore this uses O(logn) amount of additional space.
    Running time is O(n): there are 2n-1 fn calls


'''