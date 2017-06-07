''' 
Random Walk: path with no clear direction but determined by series of random 
decisions left to chance.

Has useful applications in nature, physics, biology, and other sciences and 
etc...

So in this file we are going to create a randomwalk data and make visually 
appealing?

'''

from random import choice

# class for random walking data
class RandomWalk():
    def __init__(self, num_points=5000):
        # initialize attributes
        self.num_points = num_points

        # all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]



    def get_step(self):
        direction = choice([1,-1])
        distance = choice(list(range(9)))
        step = direction * distance
        return step

    # Calcuate all points in walk
    def fill_walk(self):

        # defining some variables here
        direction = [1, -1]
        distance = range(0, 7)

        # take steps until desired length
        # simulates 4 random decisions
        while len(self.x_values) < self.num_points:
            # decide which direction to go and how far to go
            # 1 for right, -1 for left
            x_step = self.get_step()
            y_step = self.get_step()

            # rejects move that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    

