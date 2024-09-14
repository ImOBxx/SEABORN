import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Define a function to create the line plot
def graph():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)

# Create a figure object with specified size
fig = plt.figure(figsize=(5, 4))

# Add the main plot (axes) to the figure
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
graph()  # Create the line plot on the main axes

# Add an inset plot (axes) within the main plot
ax2 = fig.add_axes([0.5, 0.5, 0.3, 0.3])
graph()  # Create the line plot on the inset axes

# Display the plot
plt.show()
