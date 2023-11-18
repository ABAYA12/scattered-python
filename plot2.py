import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# set a title foe the plot
plt.title('X Power 2 Values')

# plot the graph with scatter() and pass in x and y values
plt.scatter(x_values, y_values, edgecolors='yellow', s=40)

# set names for both x and y axis
plt.xlabel('Vales of X')
plt.ylabel('Vales of Y in Thousands')

# set the axis for both x and y with a given range
plt.axis([0, 1100, 0, 1100000])
# display the graph
plt.show()
