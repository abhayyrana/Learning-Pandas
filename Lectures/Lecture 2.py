# ANALYSIS OF DATA

import pandas as pd

df = pd.read_csv("DataSets/StudentsPerformance.csv", encoding="latin-1")

# head() and tail() of a dataset
print("Display first 5 rows of the dataset:")
print(df.head(5))
print("Display last 5 rows of the dataset:")
print(df.tail(5))

# info() of the dataset
print("Display the information about the dataset:")
print(df.info())

# describe() summary of the dataset
print("Display the statistical description of the dataset:")
print(df.describe())

# shape and columns of the dataset
print(f"Shape of the dataset: {df.shape}")
print(f"Columns in the dataset: {df.columns}")
