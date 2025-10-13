#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        13/10/2025           Write a python function to divide two numbers and 
#                                                handle ZeroDivisionError, ValueError or any other Exception.


# A try statement can have more than one except clause, to specify handlers for different exceptions. 
# Please note that at most one handler will be executed. 


def division(num1=0, num2=0):
    try:
        return int(num1) / int(num2)
    except ZeroDivisionError:
        return -1
    except ValueError:
        return -2
    except Exception as err: # This will handle any other exception
        print("Error Type:", type(err))
        print("Error:", err)
        return -3

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

result = division(num1, num2)
print(f"Result: {result}")
