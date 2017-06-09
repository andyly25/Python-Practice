from random import randint

# class represent a single die
class Die():
    # assumption 6 sided die
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    # return random # based on num of sides
    def roll(self):
        return randint(1, self.num_sides)
