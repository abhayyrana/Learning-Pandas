# MERGING AND CONCATINATING DATAFRAMES

import pandas as pd

df_customer = pd.DataFrame({
    'Customer ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
})

df_orders = pd.DataFrame({
    'Customer ID': [1, 2, 4, 6, 7],
    'Order Amount': [250, 150, 300, 400, 500]
})

# merging of datasets
## inner join
df_merged = pd.merge(df_customer, df_orders, on='Customer ID', how='inner')
print("\nInner Join")
print(df_merged)
## outer join
df_merged = pd.merge(df_customer, df_orders, on='Customer ID', how='outer')
print("\nOuter Join")
print(df_merged)
## left join
df_merged = pd.merge(df_customer, df_orders, on='Customer ID', how='left')
print("\nLeft Join")
print(df_merged)
## right join
df_merged = pd.merge(df_customer, df_orders, on='Customer ID', how='right')
print("\nRight Join")
print(df_merged)
## cross join
df_merged = pd.merge(df_customer, df_orders, how='cross')
print("\nCross Join")
print(df_merged)

# concatenation of dataset
df_concat = pd.concat([df_customer, df_orders], axis=1, ignore_index=True)
''' Syntax: pd.concat([df1, df2], axis=0(rows)/1(columns), ignore_index=True/False)
'''
print(df_concat)
