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

    # Calcuate all points in walk
    def fill_walk(self):

        # take steps until desired length
        # simulates 4 random decisions
        while len(self.x_values) < self.num_points:
            # decide which direction to go and how far to go
            # 1 for right, -1 for left
            x_direction = choice([1,-1])
            x_distance = choice([0, 1, 2,3,4])
            # determine length of each step in x direction 
            x_step = x_direction * x_distance

            # 1 for up, -1 for down
            y_direction = choice([1,-1])
            y_distance = choice([0, 1, 2,3,4])
            # determine length of each step in y direction 
            y_step = y_direction * y_distance

            # rejects move that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

