from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns   

sns.displot(random.poisson(lam = 2, size = 2000), kde = False)

plt.show()