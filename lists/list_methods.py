list1 = [1, 2, 3, 4, 5]
list1.append(6)  # Add an element to the end of list1.
print(list1)

list2 = [7, 8, 9]
list1.extend(list2)  # Add list2 to the end of list1.
print(list1)

list1.insert(2, "2A")  # Insert a new element at a specific index in the list.
print(list1)

list1.remove("2A")  # Remove an item by name.
print(list1)

list1.pop()  # Remove the last item from list1.
print(list1)

# Remove the last item from list1 and assign that item as a variable.
removed = list1.pop()
print(removed)

list1.pop(1)  # Remove item from list1 at index 1.
print(list1)

# Remove item from list1 at index 2 and assign it to a variable.
removed = list1.pop(2)
print(removed)

# Remove all elements from a list
list2.clear()
print(list2)

# Find item in list and return index number.  Range arguments are optional.
index = list1.index(1, 0, 2)
print(index)

# Return the number of times an elements appears in a list.
times = list1.count(1)
print(times)

# Sort a list
list3 = [7, 2, 5, 6, 8, 3, 10, 1]

# Return a list sorted
list3_sorted = sorted(list3)
print(list3_sorted)

# Sort a list in place
list3.sort()
print(list3)

# Reverse the order of the elements in a list
list3.reverse()
print(list3)

# Return a shallow copy of a list
list3_copy = list3.copy()
print(list3_copy)
