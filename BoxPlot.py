import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("iris")

sns.boxplot(x = "sepal_length", y = "sepal_width", data = data)

plt.show()