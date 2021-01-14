import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# First Graph - 1

# Defining the X axis and Y axis values as lists...
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Resizing the gragh size to show them bigger or smaller as required...
plt.figure(figsize=(5,3), dpi=125)

# To plot and display the graph with customised graph properties like color, linewidth, linestyle, marker, markersize, amrkeredgecolor, etc...
plt.plot(x, y, label='D vs T', color='green', linewidth=3, linestyle='--', marker='.', markersize=15, markeredgecolor='red')

# Shortcut Notation...
# fmt = '[color][marker][line]'
#plt.plot(x, y, 'b+-', label='D vs T')
#plt.plot(x, y, 'b*--', label='D vs T')

# Second Graph - 2

# Defining X axis values to be plotted with Start value, End value, Incremental value using numpy's arange method...
x2 = np.arange(0, 5, 0.5)

# Plotting the 2nd graph with x2 in X axis and square of x2 in Y axis...
#plt.plot(x2, x2**2, 'r^-', label='x vs x^2')

# Plotting the 2nd graph with x2 in X axis with 2 different line styles and square of x2 in Y axis...
plt.plot(x2[:7], x2[:7]**2, 'r', label='x vs x^2')
plt.plot(x2[6:], x2[6:]**2, 'r--')


# To define a title with specific font and size...
plt.title('My First Graph : Distance vs Time', fontdict={'fontname': 'Verdana', 'fontsize': 25})

# To define X axis attribute with specific font and size...
plt.xlabel('Time (Minutes)', fontdict={'fontname': 'Times New Roman', 'fontsize': 15})

# To define Y axis attribute with specific font and size...
plt.ylabel('Distance (KM)', fontdict={'fontname': 'Times New Roman', 'fontsize': 15})

# To define the X axis range...
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# To define the Y axis range...
plt.yticks([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# To define a legend for the graph line...
plt.legend()

# To display graph in Pycharm. Not required for JupyterLab and graph will get displayed automatically...
#plt.interactive(False)

# To remove the string appearing representing the graph ID or name...
plt.show()

# To save the graph by giving an image name and this will be saved by default into the location where main.py file exists...
#plt.savefig('Line_Graph_1.jpeg', dpi=150)
#plt.savefig('Line_Graph_1.jpeg')


# Bar Chart

# Defining the labels as X axis for the barchart...
labels = ['Apples', 'Strayberrys', 'Oranges']

# Defining the equivalent values as Y axis for the barchart...
values = [5, 15, 10]

# Resizing the gragh size to show them bigger or smaller as required...
plt.figure(figsize=(6, 3), dpi=125)

# To plot and display the barchart
#plt.bar(labels, values)


# Option 1 - Defining patterns for each of the bars as per defined labels...
#mybars = plt.bar(labels, values)
#mybars[0].set_hatch('.')
#mybars[1].set_hatch('/')
#mybars[2].set_hatch('*')

# Option 2 - Alternative way to define patters for each of the bars as per defined labels...
mybars = plt.bar(labels, values)
patterns = ['+', '*', '|']
for b in mybars:
    b.set_hatch(patterns.pop(0))

# To define a title with specific font and size...
plt.title('My Bar Chart : Fruits', fontdict={'fontname': 'Verdana', 'fontsize': 25})

# To remove the string appearing representing the graph ID or name...
plt.show()


# To save the graph by giving an image name and this will be saved by default into the location where main.py file exists...
#plt.savefig('Bar_Chart_1.jpeg', dpi=150)


