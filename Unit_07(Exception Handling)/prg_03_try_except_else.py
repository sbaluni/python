#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        13/10/2025           Write a python function to divide two numbers and 
#                                                handle some basic exceptions using try, except and else.


# In Python, you can also use the else clause on the try-except block which must be present after 
# all the except clauses. The code enters the else block only if the try clause does not 
# raise an exception.


def division(num1=0, num2=0):
    c = 0
    try:
        c = int(num1) / int(num2)
    except ZeroDivisionError:
        return -1
    except ValueError:
        return -2
    except Exception as err: # This will handle any other exception
        print("Error Type:", type(err))
        print("Error:", err)
        return -3
    else:
        return c

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

result = division(num1, num2)
print(f"Result: {result}")
