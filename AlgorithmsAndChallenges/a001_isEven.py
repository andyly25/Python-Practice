'''
    I've noticed the question of determining if a number is an even number 
    often, and it seems easy as you can just use modulo 2 and see if 0 or some 
    other methods with multiplication or division.
    But here's the catch, I've seen a problem that states:
    You cannot use multiplication, modulo, or division operators in doing so.

    So what does that leave? Bitwise operators:
    here's a small tutorial on them:
    AND: 1 & 1 = 1
    OR: 0 | 1 = 1, 1 | 0 = 1, 1 | 1 = 1
    XOR: 0^1 = 1 , 1^0 = 1
    NOT: !0 = 1

    Here's an example with AND
    010 : 2
    011 : 3
    ----
    010 : 2

    now using that 2 & with 010 : 1

    010 : 2
    001 : 1
    ----
    000 : 0

    thus we can say that even numbers &1 gives 0
'''

def is_even(k):
    if((k&1)==0):
        return True;
    return False;

# x = input("Input an int")
num1 = 3
num2 = 50
num3 = 111111111111

print("is num1 even? ", is_even(num1))
print("is num2 even? ", is_even(num2))
print("is num3 even?", is_even(num3))