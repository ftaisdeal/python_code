import pandas as pd

df = pd.read_csv('pandas/data.csv')

print(df.head(10))

# If a number of rows is not specified, the default is 5
print(df.head())

print(df.tail())

print(df.info()) # Returns information about the dataset