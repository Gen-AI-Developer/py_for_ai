# List Slicing in Python - Tutorial

# List slicing allows you to extract parts of a list using the slice notation: list[start:stop:step]

# 1. Basic Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original list:", numbers)

# Get elements from index 2 to 5 (excluding 5)
print("numbers[2:5]:", numbers[2:5])  # [2, 3, 4]

# Get elements from start to index 4 (excluding 4)
print("numbers[:4]:", numbers[:4])    # [0, 1, 2, 3]

# Get elements from index 6 to end
print("numbers[6:]:", numbers[6:])    # [6, 7, 8, 9]

# 2. Using Step
# Get every second element from index 1 to 7
print("numbers[1:8:2]:", numbers[1:8:2])  # [1, 3, 5, 7]

# Get every third element from the whole list
print("numbers[::3]:", numbers[::3])      # [0, 3, 6, 9]

# 3. Negative Indices
# Get last 3 elements
print("numbers[-3:]:", numbers[-3:])      # [7, 8, 9]

# Get elements from index -7 to -2 (excluding -2)
print("numbers[-7:-2]:", numbers[-7:-2])  # [3, 4, 5, 6, 7]

# 4. Negative Step (Reverse Slicing)
# Reverse the list
print("numbers[::-1]:", numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Get every second element in reverse
print("numbers[::-2]:", numbers[::-2])    # [9, 7, 5, 3, 1]

# 5. Omitting Indices
# Omitting start and stop uses the whole list
print("numbers[:]:", numbers[:])          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 6. Slicing Assignment
# Replace part of the list
numbers[2:5] = [20, 30, 40]
print("After assignment:", numbers)       # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# 7. Slicing with Strings (works similarly)
text = "PythonList"
print("text[1:5]:", text[1:5])            # "ytho"
print("text[::-1]:", text[::-1])          # "tsiLnohtyP"

# 8. Edge Cases
# Start > Stop with positive step returns empty list
print("numbers[5:2]:", numbers[5:2])      # []

# Start < Stop with negative step returns empty list
print("numbers[2:5:-1]:", numbers[2:5:-1])# []

# 9. Copying a List
copy = numbers[:]
print("Copy of list:", copy)

# Summary:
# list[start:stop:step]
# - start: index to start (inclusive)
# - stop: index to stop (exclusive)
# - step: increment (default 1), can be negative for reverse

# Slicing is a powerful way to access, modify, and copy parts of lists and other sequences in Python.