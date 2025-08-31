# DATA SEGREGATION

import pandas as pd

df = pd.read_csv("DataSets/StudentsPerformance.csv", encoding="latin-1")

# selecting columns
## selecting single column
print("Gender of the students:")
print(df["gender"])
## selecting multiple columns
subset = df[['parental level of education', 'gender']]
print("Subset of the dataset with selected columns:")
print(subset)

# filtering rows
## selecting single row
math_marks = df[df['math score'] == 100]
print("\nStudents with math score equal to 100:")
print(math_marks)
## selecting multiple rows
multi_marks = df[(df['math score'] == 100) & (df['reading score'] == 100)]
print("\nStudents with math and reading score equal to 100:")
print(multi_marks)

# using 'OR' condition
or_condition = df[(df['math score'] == 100) | (df['reading score'] == 100)]
print("\nStudents with either math or reading score equal to 100:")
print(or_condition)
