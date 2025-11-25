# Define a lambda function to calculate the power of a number. 
# Function body is after the :.
# Return keyword is infered.
# Use cases are for simple functions
# probably inside other code(function | declarations etc)
#
# Parameters:
#   base (int or float): The base number to be raised to a power.
#   exp (int or float): The exponent indicating the power to which the base is raised.
# Returns:
#   The result of raising `base` to the power of `exp` using the `**` operator.
power_to = lambda base, exp: base ** exp

print(power_to(2, 2))  # Output: 4
print(power_to(2, 3))  # Output: 8
print(power_to(2, 10)) # Output: 1024
print(power_to(3, 2))  # Output: 9
print(power_to(10, 3)) # Output: 1000

def main():
    # Define a lambda function to calculate the power of a number.
    # Parameters:
    #   base (int or float): The base number to be raised to a power.
    #   exp (int or float): The exponent indicating the power to which the base is raised.
    # Returns:
    #   The result of raising `base` to the power of `exp` using the `**` operator.
    power_to = lambda base, exp: base ** exp

    print(power_to(2, 2))  # Output: 4
    print(power_to(2, 3))  # Output: 8
    print(power_to(2, 10)) # Output: 1024
    print(power_to(3, 2))  # Output: 9
    print(power_to(10, 3)) # Output: 1000
    print(power_to(2, 10000000))  # ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

if __name__ == '__main__':
    main()