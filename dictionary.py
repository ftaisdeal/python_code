# Dictionary comprehension builds a dictionary from an iterable
results = {n: n ** 2 for n in range(10)}

print(results)
print(results.keys())
print(results.values())
print(results.items())
