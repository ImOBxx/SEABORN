import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("iris")

def plot():
    sns.lineplot(x = "sepal_length", y = "sepal_width", data = data)

sns.set_palette('vlag')
plt.subplot(211)

plot()

sns.set_palette('Accent')
plt.subplot(212)
plot()

plt.legend()
plt.show()
