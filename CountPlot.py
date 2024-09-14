import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("iris")

sns.countplot(x = "sepal_length", data = data)

plt.show()