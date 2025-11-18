# FIRST WAY TO IMPORT STUFF FROM FILE - import whole file
# import my_calculations

# num2 = 200

# res = my_calculations.my_add_function(10, 20)
# print(res)

# res1 = my_calculations.my_add_function(my_calculations.num1, num2)
# print(res1)

# SECOND WAY - import what I need
# from my_calculations import my_add_function, num1

# num2 = 200

# res = my_add_function(10, 20)
# print(res)

# res1 = my_add_function(num1, num2)
# print(res1)

# THIRD WAY - import what I need WITH ALIASES
from my_calculations import my_add_function as my_add
from my_calculations import num1

num2 = 200

res = my_add(10, 20)
print(res)

res1 = my_add(num1, num2)
print(res1)
print(f"Name of __name__ in app.py: {__name__}")
