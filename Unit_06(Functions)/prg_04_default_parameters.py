#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        05/08/2025           Write a python function to add two numbers.
#                                                If no parameter is passed then default parameter value to 0.


def addition(p_num1 = 0, p_num2 = 0):
    return p_num1 + p_num2


num1 = int(input('Enter first number:'))

# Call to function. 
# Here we are not passing second parameter p_num2. In function it's default value 0 will be taken.
s = addition(p_num1 = num1)
print("Sum:", s)

