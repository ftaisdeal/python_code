import pandas as pd

df = pd.read_csv('pandas/data_2.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

# This script in its current form does not work.