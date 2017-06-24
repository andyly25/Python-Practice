# was curious when I saw the word generator mentioned a couple of time
# and I didn't exactly know how to use so here's an example:

def fibonacci(n):
    """A generator for fibonacci nums"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter >n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)
for x in f:
    print (x, " ", end="")
print()


'''
Sample of *arg and **kwargs
'''
# testing *arg out
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv: ", arg)

test_var_args('Justin', 'feena', 'guido', 'gawain')

# testiing **kwargs
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" %(key, value))

greet_me(name="klokkers")


# decorating generators
from functools import wraps

def get_ready(gen):
    """
    Decorator: gets generator ready by advancing to first yield statement
    Note: have no idea what functools.wrap does so here's a google:
        This takes a function used in a decorator and adds the functionality
        of copying over the function name, docstring, args list, etc. And 
        wraps itself is a decorator.
    Now... what is a decorator?
        provide a simple syntax for calling higer order functions. 
        soo.. a function that takes another func and extends the behavior of 
        the latter funct w/o explicitly modifying it.
        Basically the @ sumbol you see before some things

    Yay, more unfamilliar looking things:
        *args and **kwargs can just be *var and **vars, but like so for convention.
        They are mostly used in function definitions. Allow you to pass a variable
        number of args to a funct. 
        You do not know beforehand how many args will be passed to function by
        the user so you use these two keywords. 

        *args used to send a non-keyworded variable length arg list to function
        **kwargs allow pass keyworded variable length of arguments to a funct.
            is used if you want to handle named arguments in a function
    """
    @wraps(gen)
    def generator(*args, **kwargs):
        g = gen(*args, **kwargs)
        next(g)
        return g
    return generator


@get_ready
def infinite_looper(objects):
    count = -1
    message = yield None
    while True:
        if message!= None:
            count = 0 if message < 0 else message
        count += 1
        if count >= len(objects):
            count = 0
        message = yield objects[count]

# seems like this loops forever around what was passed inside
x = infinite_looper("abcdef")
print(next(x))
print(x.send(4))
print(next(x))
print(next(x))
print(x.send(5))
print(next(x))

'''
    Let's do a permutation example.
    Permutations is a rearrangement of elements of an ordered list.
    Every arrangement of n elements is called a permutation
        example:
            abc
            acb
            bac
            bca
            cab
            cba
'''

def permutations(items):
    n = len(items)
    if n == 0: yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i] + items[i+1:]):
                yield[items[i]] + cc
# each 3 letters to their own lines
for p in permutations(['r', 'e', 'd']): print(''.join(p))
# this separated by comma and space
for p in permutations(list("game")): print(''.join(p) + ", ", end="")


