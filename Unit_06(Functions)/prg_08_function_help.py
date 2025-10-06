#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        06/08/2025           Write a python function sum with docstring and demonstrate
#                                                how to see the help for the function.


# Function sum with docstring defined.
def sum ( num1 = 0, num2 = 0):
    """
    This function takes two arguments num1 and num2 as input and returns sum of both numbers.
    It takes two arguments:
    num1: The first number. Default 0.
    num2: The second number. Default 0.
    """
    return num1 + num2

print(sum(2,3))

# display help for print function
help(print)

# Display help for sum function defined above. It prints function signature along with docstring
help(sum)

# We can also use __doc__ attribute to get docstring defined in function
print(sum.__doc__)
