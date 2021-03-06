import pandas as pd

"""# Use sep= "|" while reading the data"""

Users=pd.read_csv("/content/users.txt")
Users['user_id|age|gender|occupation|zip_code'].str.split("|",expand=True)
#users.set_index("user_id|age|gender|occupation|zip_code",inplace=True)
print(Users)

"""# Assign it to a variable called users and use the 'user_id' as index"""

users=pd.read_excel("/content/Book1.xlsx")
users.set_index("user_id",inplace=True)
print(users)

"""# See the first 10 and last 10 entries"""

print("--------First 10 entries -------")
print()
print(users.head(10))
print("--------Last 10 entries -------")
print()
print(users.tail(10))

"""# What is the number of observations in the dataset?"""

users_rows = users.shape[0]
print("Number of Observations : " ,users_rows)

"""# What is the number of columns in the dataset?"""

users_columns = users.shape[1]
print("Number of Columns : " ,users_columns)

"""# Print the name of all the columns."""

users.columns

"""# How is the dataset indexed?"""

users.index

"""# What is the data type of each column?"""

users.info()

"""# Print only the occupation column"""

users["occupation"]

"""# How many different occupations are in this dataset?
"""

dif_occupations = users["occupation"].unique()
print(len(dif_occupations))

"""# What is the most frequent occupation?"""

users["occupation"].mode()

"""# DataFrame Info."""

users.info()

"""# Describe all the columns"""

users.describe()

"""# Summarize only the occupation column"""

users.occupation.value_counts()

"""# What is the mean age of users?"""

users["age"].mean()

"""# What is the age with least occurrence?"""

users["age"].min()
