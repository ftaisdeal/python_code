# a list comprehension
from math import pi

cubes = [i**3 for i in range(5)]
print(cubes)

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

a = [i for i in range(20) if i % 3 == 0]
print(a)

squares1 = []
for x in range(10):
    squares1.append(x**2)
print(squares1)

squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)

squares3 = [x**2 for x in range(10)]
print(squares3)

vec = [-4, -2, 0, 2, 4]
new = [x * 2 for x in vec]
print(new)

new2 = [x * 2 for x in vec if x >= 0]
print(new2)

new3 = [abs(x) for x in vec]
print(new3)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
fruits = [fruit.strip() for fruit in freshfruit]
print(fruits)

tuples = [(x, x**2) for x in range(10)]
print(tuples)

vec2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for elem in vec2 for num in elem]
print(flattened)

pi_places = [str(round(pi, i)) for i in range(1, 10)]
print(pi_places)
