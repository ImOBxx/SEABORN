import seaborn as sns 

flights = sns.load_dataset("flights")

flights = flights.pivot("month", "year", "passengers")

print(flights)