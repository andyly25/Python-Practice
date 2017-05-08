#Testing out importing from python libraries

from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        num = randint(1, self.sides)
        print("You rolled a ... " + str(num))

class Die20(Die):
    def __init__(self):
        super().__init__()
        self.sides = 20
    # def roll_die(self):
    #     num = randint(1, self.sides)
    #     print("Shallala 20 sided die GOOO... " + str(num))

dice6 = Die()
print("Rolling the 6 die")
for x in range(0,5):
    dice6.roll_die()

#directly modifying attributes
print("\nNow for the 10 die")
dice10 = Die()
dice10.sides = 10
for y in range(0,3):
    dice10.roll_die()

#inheriting from Die 
print("\nNow for the 20 die")
dice20 = Die20()
for z in range(0,5):
    dice20.roll_die()