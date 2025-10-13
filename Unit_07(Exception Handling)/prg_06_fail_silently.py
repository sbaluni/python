#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        13/10/2025           Write a python function to divide two numbers and 
#                                                if ZeroDivisionError exception occurs, fail silently.

# Fail silently means that the program should not crash or display an error message 
# when the exception occurs.


# Don't do anything when an exception is raised using pass.
# The pass statement in Python is a null operation; it does nothing when executed. 
# Its primary purpose is to serve as a placeholder where a statement is syntactically required, 
# but no code needs to be executed immediately.
def division(num1=0, num2=0):
    try:
        return num1 / num2
    except ZeroDivisionError:
        pass

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = division(num1, num2)
print(f"Result: {result}")
