import numpy as np

array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]

np_array1 = np.array(array1)
np_array2 = np.array(array2)

bmi = np_array1 / np_array2 ** 2

print(bmi)