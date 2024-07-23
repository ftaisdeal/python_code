# Create a simple Pandas DataFrame
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

# Refer to row index:
print(df.loc[0])
print(df.loc[[0, 1]])
print(df.loc[[1, 2]])
