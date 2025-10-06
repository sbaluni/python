#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        06/10/2025           Write a python function to divide two numbers and 
#                                                handle divide by zero exception. If exception occurs,
#                                                return -1.

# Handle ZeroDivisionError exception in function
def division(num1=0, num2=0):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return -1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = division(num1, num2)
print(f"Result: {result}")
