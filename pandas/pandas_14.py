import pandas as pd

df = pd.read_csv('pandas/data.csv')

df["Calories"].fillna(130, inplace = True)

# This script in its current form produces an error.