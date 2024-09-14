import seaborn as sns 
import matplotlib.pyplot as plt 

palette = sns.color_palette('PiYG', 11)

palette1 = sns.color_palette('Greens', 11)

palette2 = sns.color_palette()

sns.palplot(palette2)

sns.palplot(palette1)

sns.palplot(palette)

plt.show()