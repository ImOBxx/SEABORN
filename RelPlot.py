import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("iris")

sns.relplot(x = "sepal_width", y = "species", data = data)

plt.show()