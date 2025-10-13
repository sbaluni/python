#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        13/10/2025           Write a python function to divide two numbers and 
#                                                handle some basic exceptions using try, except, else and finally.


# Python provides a keyword finally, which is always executed after the try and except blocks. 
# The final block always executes after the normal termination of the try block or 
# after the try block terminates due to some exception.


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
    finally:
        print("Execution completed.")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

result = division(num1, num2)
print(f"Result: {result}")
