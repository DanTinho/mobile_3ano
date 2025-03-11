# Arrays (we'll use the numpy library)
import numpy as np

# Create an array
array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

# Acessing elements
print("First element:", array[0])
print("KLast element:", array[-1])

# Slicing
print("Elements from 1 to 3:", array[1:3])

# List
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Append an element
my_list.append(6)
print("List after append:", my_list)

# Insert an element on a specific position
my_list.insert(2, 7)
print("List after insert:", my_list)

# Remove an element
my_list.remove(4)
print("List after remover:", my_list)

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Acessing elements (same as list)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Loops
# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
i = 0
while i < 5:
    print(i)
    i +=  1

# Looping over a list with indices
my_list = [1, 2, 3, 4, 5]
for i, element in enumerate(my_list):
    print(f"Index {i}: {element}")

    