""" Simple scatter plot """
import matplotlib.pyplot as plt


# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# Here we make a larger list using range and also a for loop
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

x_cubed = list(range(1,1001))
y_cubed = [xc**3 for xc in x_values]


# call scatter and s sets size of the dots
# here we use a color map, used to emphasize a pattern in data.
# pyplot includes built in color maps.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
    edgecolor='none', s=40)

plt.scatter(x_cubed, y_cubed, c=y_cubed, cmap=plt.cm.Reds,
    edgecolor='none', s=40)

# Set the chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14, length='7')
# plt.tick_params(which='minor', length=4, color='r')

plt.axis([0, 1100, 0, 1100000])

# if you want program to auto save plot to file, you can replace plt.show()
# with plt.savefig(). First arg shows where to save, and second trims xtra 
# whitespace from plot
plt.savefig('e02_simpleScatter.png', bbox_inches='tight')
plt.show()

