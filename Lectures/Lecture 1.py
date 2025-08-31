# READING & SAVING DATA TO DIFFERENT FILE FORMATS

import pandas as pd

# read data from csv file into a data frame
df_csv = pd.read_csv("DataSets/StudentsPerformance.csv", encoding="latin-1")
''' Encodings are of 2 types: "utf-8" or "latin-1" '''
df_excel = pd.read_excel("DataSets/Superstore.xlsx")
df_json = pd.read_json("DataSets/books.json")
''' 
    for reading data stored in a cloud storage, we can use "gcsfs" library
'''
print(df_csv)
print(df_excel)
print(df_json)

data = {
    "Name": ['Ram', "Shyam", "Ghanshyam"],
    "Age": [10, 20, 30],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False)
''' "index=False" means that indexing will not be performed in the output file. '''
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False, orient="records", lines=True)
''' orient "records" means that each line will contain a separate JSON object. 
    lines=True means that the output will be in a line-delimited JSON format. '''
