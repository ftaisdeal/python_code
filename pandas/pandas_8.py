import os
import pandas as pd

df = pd.read_csv('pandas/data_1.csv')

print(pd.options.display.max_rows) # Show maximum rows setting within Pandas

pd.options.display.max_rows = 100 # Set maximum rows to display

print(df)

print(df.to_string()) # Using the to_string method