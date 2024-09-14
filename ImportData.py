import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('ComputerSales.csv')

print(df.head(5))

print(sns.get_dataset_names())