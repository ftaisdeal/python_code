# You can also use a key/value object, like a dictionary, when creating a Series.
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)