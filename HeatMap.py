import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("tips")

tc = data.corr()

sns.heatmap(tc)

plt.show()