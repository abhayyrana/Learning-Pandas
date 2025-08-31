# CLEANING OF MISSING DATA

import pandas as pd

data = {
    "Name": ['Ram', None, "Ghanshyam"],
    "Age": [10, 20, None],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)
print(df)

# detecting missing values
print(df.isnull())
print(df.isnull().sum())

# removing missing values
df.dropna(axis = 0, inplace=True)
''' Syntax: df.dropna(axis=0, inplace=True)
    axis=0: Drop rows with missing values
    axis=1: Drop columns with missing values
'''
print(df)
