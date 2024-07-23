import pandas as pd

df = pd.read_csv('pandas/data2.csv')

# If you want to change the original DataFrame, use the inplace = True argument.
df.dropna(inplace = True)

print(df.to_string())