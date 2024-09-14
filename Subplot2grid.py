import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Define a function to create the line plot
def graph():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)

axes1 = plt.subplot2grid (
  (7, 1), (0, 0), rowspan = 2, colspan = 1) 
graph()

axes2 = plt.subplot2grid (
  (7, 1), (2, 0), rowspan = 2, colspan = 1) 
graph()

axes3 = plt.subplot2grid (
  (7, 1), (4, 0), rowspan = 2, colspan = 1) 
graph()

plt.show()