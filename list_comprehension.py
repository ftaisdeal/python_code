# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

a = [i for i in range(20) if i % 3 == 0]
print(a)
