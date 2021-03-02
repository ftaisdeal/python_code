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

list2.clear()
print(list2)
