import pandas as pd

df = pd.read_csv('pandas/data_2.csv')

# The fillna() method allows you to replace empty cells with a value.
df.fillna(130, inplace = True)

print(df.to_string())