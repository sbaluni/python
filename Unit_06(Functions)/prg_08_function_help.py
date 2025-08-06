#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        06/08/2025           Write a python function that accepts arbitrary number 
#                                                of arguments for a user profile. E.g. first_name, last_name,
#                                                location, field etc.. 


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
