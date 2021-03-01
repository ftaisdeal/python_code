# Multiple variables can be assigned at once
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Variables can be "unpacked" from a list
fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)
print(y)
print(z)

# Output of variables can be concatenated
x = "awesome"
print("Python is " + x)

# String variables can be concatenated into new variables
x = "Python is "
y = "awesome"
z = x + y
print(z)

# Global variables are variables createed outside of a functioon.
# These variables are available everywhere within a script, including within functions.
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.


def myfunc2():
    global y
    y = "great"


myfunc2()

print("Python is " + y)
