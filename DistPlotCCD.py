import pandas as pd
import matplotlib .pyplot as plt
import seaborn as sns  

crash_df = sns.load_dataset('test-new.csv')

print(crash_df.head(5))