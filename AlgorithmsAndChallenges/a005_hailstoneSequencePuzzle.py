# NOTE: I just discovered Python 3 has / for floating point division
# and // for integer division... now it makes sense

'''
    1. Pick pos integer n as start
    2. if n is even, divide by 2
    3. if n is odd, multiply by 3 and add 1
    4. continue until n is 1

    Goal, try to write recursive function

    I was looking around at puzzles and saw this at stack overflow
    https://stackoverflow.com/questions/39507395/the-recursive-implementation-with-python-for-a-mathematical-puzzle-of-hailstone
    Would be a good reference.
'''

# recursive process
def hailstone(n):
    # starting with the ending condition when n is 1
    if n == 1:
        print(str(n) + " 1" )
        return (n,), 1

    # now to see if it's even
    if n % 2 == 0: 
        rest = hailstone(n//2)
    # now for odd
    else:
        rest = hailstone(n*3 + 1)
    print(str(n) + " " + str(rest[0]) + " " + str(rest[1]+1))
    return (n, ) + rest[0], rest[1] + 1


# ______________________________________________
# iterative process, helpful with a helper function
# When recursing here, we pass next n in series and result so far.
def hailstone2(n):
    # call helper with initial values set
    return hailstoneHelper(n, (), 0)

def hailstoneHelper(n, seq, length):
    # begin with end condition
    if n == 1:
        print("sequence "+ str(seq) + " "+ str(n) + " length " + str(length+1))
        return seq + (n, ), length + 1
    # if even
    if n % 2 == 0: 
        return hailstoneHelper(n//2, seq + (n,), length + 1)
    else:
        return hailstoneHelper(n*3 + 1, seq + (n,), length + 1)

#_______________________________________________
# A more pythonic solution
def hailstone3(n):
    seq = []
    while n!= 1:
        seq.append(n)
        if n%2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    seq.append(n)
    print(str(tuple(seq)) + " sequence length " + str(len(seq)))
    return tuple(seq), len(seq)

print("\npythonic method")
hailstone3(7)
print('\niterative method')
hailstone2(7)
print("\nrecursive method")
hailstone(7)