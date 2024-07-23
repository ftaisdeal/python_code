import pandas as pd

df = pd.read_csv('pandas/data2.csv')

new_df = df.dropna()

print(new_df.to_string())