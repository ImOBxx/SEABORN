from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns   


sns.distplot(random.exponential(size = 1000), hist = False)

plt.legend()

plt.show()