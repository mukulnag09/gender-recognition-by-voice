import matplotlib.pyplot as plt
import numpy as np

# Create some data to plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Set up the figure and axes
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_title('A simple line plot')

# Save the plot as a PNG file
plt.savefig('my_plot.png')