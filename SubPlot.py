import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("iris")

def graph():
    sns.lineplot(x = "sepal_length", y = "sepal_width", data = data)

plt.subplot(121)

graph()

plt.subplot(122)

graph()

plt.show()