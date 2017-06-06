'''
1. import pyplot module and using alias plt to make life easier.
2. create a lit to hold some numerical data.
3. pass into plot() function to try plot nums in meaningful way.
4. after launching, shows you simple graph that you can navigate through.
'''

# 1
import matplotlib.pyplot as plt

# input values will help set what the x-axis values would be
input_values = [1, 2, 3, 4, 5]

# 2
squares = [1, 4, 9, 16, 25]

# 3
# line width controls thickness of line plot() generates.
plt.plot(input_values, squares, linewidth=5)

# set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
