import pandas as pd

# Sample data
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-02-01'],
    'Region': ['North', 'South', 'North'],
    'Product': ['A', 'B', 'A'],
    'Amount': [100, 150, 200]
}

df = pd.DataFrame(data)

# Create a pivot table
pivot_table = df.pivot_table(values='Amount', index='Region', columns='Product', aggfunc='sum', fill_value=0)

print(pivot_table)