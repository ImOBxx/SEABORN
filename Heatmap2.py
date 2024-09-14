import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

data = np.random.randint(low = 1,
                         high = 100,
                         size = (10, 10))

xticklabels = True
yticklabels = True

cmap = "tab20"
center = 0

linewidths = 2
linecolor = "yellow"

annot = True

hm = sns.heatmap(data = data,
                 xticklabels=xticklabels,
                 yticklabels=yticklabels,
                 cmap = cmap,
                 center=center,
                 annot = annot,
                 linewidths= linewidths,
                 linecolor=linecolor
                 )

plt.show()