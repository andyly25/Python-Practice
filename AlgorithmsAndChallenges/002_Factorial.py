# Simple practice on recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        print("current n is: " + str(n))
        return n * factorial(n-1)

print("multiply all together and you get " + str(factorial(4)))


'''
How this works is that it goes downwards from (let f be factorial)
f(4) -> f(3) -> f(2) -> f(1) -> f(0)

then starting from f(0) it starts heading back up
return 1            // f(0)
return 1*1 = 1      // f(1)
return 2*1 = 2      // f(2)
return 3*2 = 6      // f(3)
return 4*6 = 24     // f(4)
'''