# MANIPULATION OF DATA

import pandas as pd

data = {
    "Name": ['Ram', "Shyam", "Ghanshyam"],
    "Age": [10, 20, 30],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)
print(df)

# adding columns
## using square brackets []
df["Salary"] = [50000, 60000, 70000]
print(df)
## using insert()
df.insert(0, "Employee ID", [1601, 1602, 1603])
''' Syntax: df.insert(loc, column_name, data_value)
'''
print(df)

# updating values
df.loc[1, "Age"] = 21
''' Syntax: df.loc[row_index, "column_name"] = new_value
'''
print(df)

# updating values at multiple locations
df["Salary"] = df["Salary"] * 1.05
print(df)

# removing columns
df.drop(columns = ["City"], inplace=True)
''' Syntax: df.drop(columns = ["column_name"], inplace=True)
    inplace: If True, the operation is done in place and the original DataFrame is modified.
    inplace: If False, a new DataFrame is returned with the operation applied.
'''
print(df)
