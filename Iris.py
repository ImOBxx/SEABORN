import seaborn as sns 
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

#plt.figure(figsize = (10, 10))

sns.set_style("whitegrid")

sns.lineplot(x = "sepal_length", y = "sepal_width", data = data)

plt.title("Title Using Matplotlib Function")

plt.xlim(5)

sns.despine()

sns.set_context("poster")

plt.show()
