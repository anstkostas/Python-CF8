# Define the original list with mixed data types including a nested list
my_list = [1, 2, "Hello", [3, 4, 5]]

# Create a shallow copy of the original list using list slicing
new_list = my_list[:]
print("Are new_list and my_list the same object:", new_list is my_list) # Are new_list and my_list the same object: False

# Modify an immutable element (integer) in the original list
my_list[0] = 100
print("Original list after changing the first element to 100:", my_list)  # My list: [100, 2, 'Hello', [3, 4, 5]]
print("Shallow copy after changing the first element in the original list:", new_list)  # New list: [1, 2, 'Hello', [3, 4, 5]]
print("------------------------------------------------------------------------------------")

# Modify a mutable element (nested list) in the original list
my_list[3][0] = 300
print("Original list after modifying nested list:", my_list)  # My list: [100, 2, 'Hello', [300, 4, 5]]
print("Shallow copy after modifying nested list in the original list:", new_list)  # New list: [1, 2, 'Hello', [300, 4, 5]]