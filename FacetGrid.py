import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

plot = sns.FacetGrid(data, col = "species")
plot.map(plt.plot, "sepal_width")

plt.show()