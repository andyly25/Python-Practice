import pygal
from e04_die import Die

die1 = Die()
die2 = Die()

# store rolls into a list
results = []
# Using Pygal allows an increase in simulated rolls
for roll_num in range(50000):
    result = die1.roll() * die2.roll()
    results.append(result)

# ANalyze frequencies by counting how many time each num appears
frequencies = []
max_result = die1.num_sides * die2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# visualize the results
# create a bar chart by creating instance of pygal.Bar()
hist = pygal.Bar()

# make the labels
hist.title = "results of rolling D6 and D6 50000 times."
# I used hist.x_labels = list(range(1,36)) not as flexible as below
hist.x_labels = [str(x) for x in range(1, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of result"

# add series of values to the chart
hist.add("D6 x D6", frequencies)
# render chart into svg file, easiest way to view is in web browser
hist.render_to_file('e04_die_visual5.svg')