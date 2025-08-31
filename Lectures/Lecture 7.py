# SORTING AND AGGREGATION

import pandas as pd

data = pd.read_csv("DataSets/StudentsPerformance.csv")
df = pd.DataFrame(data)
df1 = df.copy()
print(df)

# sorting data
## sorting data in 1 column
df1.sort_values(by="math score", ascending=True, inplace=True)
''' Syntax: df.sort_values(by="column_name", ascending=True/False, inplace=True)
    ascending=True: Sort in ascending order
    ascending=False: Sort in descending order
'''
print(df1)

## sorting multiple columns
df1.sort_values(by=["math score", "reading score"], ascending=[True, True], inplace=True)
''' Syntax: df.sort_values(by=["col1", "col2"], ascending=True/False, inplace=True)
'''
print(df1)

# summary statistics
''' Syntax: df["column_name"].method()
'''
df["math score"].mean()
df["reading score"].median()
df["writing score"].mode()
df["math score"].std()
df["reading score"].var()
df["writing score"].min()
df["math score"].max()
df["reading score"].count()

# aggregating data
## grouping single column
group1 = df.groupby("gender")["math score"].sum()
''' Syntax: df.groupby("column_name")["target_column"].agg("function")
'''
print(group1)

## grouping multiple columns
group2 = df.groupby(["gender", "race/ethnicity"])["reading score"].mean()
print(group2)
