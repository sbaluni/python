#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        05/08/2025           Write a python function to add two numbers.


def addition(p_num1, p_num2):
    return p_num1 + p_num2


num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))

# Call to function using positional arguments
s = addition(num1, num2)
print("Sum:", s)

num3 = int(input('Enter first number:'))
num4 = int(input('Enter second number:'))

# Call to function using keyword arguments. In this case order doesn't matter.
s = addition(p_num1 = num3, p_num2 = num4)
print("Sum:", s)
