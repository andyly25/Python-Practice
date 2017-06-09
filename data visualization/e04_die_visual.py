import pygal
from e04_die import Die

die = Die()

# store rolls into a list
results = []
# Using Pygal allows an increase in simulated rolls
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# ANalyze frequencies by counting how many time each num appears
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# visualize the results
hist = pygal.Bar()

hist.title = "results of rolling one 6 sided Dice 1k times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add("D6", frequencies)
hist.render_to_file('e04_die_visual.svg')