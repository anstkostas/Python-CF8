my_tuple = 10, 20, 30, 40, 50
# a, b, c, d, e = my_tuple  # Unpacking a tuple

# Initializing a list of integers
my_list = [1, 2, 3, 4, 5]

# Simple unpacking of all elements
a, b, c, d, e = my_list
print(f"Unpacked values: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")

# Unpacking with a placeholder for unused elements (using underscore)
a, _, c, _, e = my_list
print(f"Skipping some values: a = {a}, c = {c}, e = {e}")

# Unpacking the first element, capturing the rest in a list
x, *rest = my_list
print(f"First element: x = {x}, Remaining: rest = {rest}")

# Unpacking the last element, capturing the rest in a list
*start, z = my_list
print(f"Last element: z = {z}, Starting elements: start = {start}")

# Unpacking with both the first and last elements captured, rest in the middle
first, *middle, last = my_list
print(f"First: first = {first}, Middle: middle = {middle}, Last: last = {last}")

# Attempt to unpack into more variables than elements (this will raise an error)
try:
    a, b, c, d, e, f = my_list
except ValueError as ve:
    print("Error:", ve)

# Handling cases where fewer elements are unpacked than are available
a, b, *rest = my_list
print(f"First two: a = {a}, b = {b}, Rest: rest = {rest}")

a, b, *rest = [10, 20, 30]  # a=10, b=20, rest=[30]
a, b, *rest = [10, 20]      # a=10, b=20, rest=[]
a, b, *rest = [10]          # ValueError: not enough values to unpack (expected at least 2, got 1) 
print(f"a={a}, b={a}, rest={rest}")