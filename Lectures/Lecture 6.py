# FILLING OF MISSING DATA

import pandas as pd

data = {
    "Name": ['Ram', None, "Ghanshyam"],
    "Age": [20, 30, None],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)
df1 = df.copy()
df2 = df.copy()
df3 = df.copy()
df4 = df.copy()
print(df)

# using fillna()
df.fillna(value={"Name": "Unknown", "Age": 0, "City": "Unknown"}, inplace=True)
''' Syntax: df.fillna(value={"column_name": value}, inplace=True)
'''
print(df)

# filling a calculated value
df1.fillna(df1["Age"].mean(), inplace=True)
''' Syntax: df.fillna(value, inplace=True)
    Here, value can be a scalar, dictionary, or Series.
'''
print(df1)

# using interpolation
## linear interpolation
df2["Age"] = df2["Age"].interpolate(method="linear", axis=0)
print(df2)

''' Other types of interpolation you should know:
        1. Polynomial Interpolation
        2. Spline Interpolation
        3. Time Interpolation
'''
