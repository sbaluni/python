#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        13/10/2025           Write a python function to divide two numbers and 
#                                                raise exception if denominator is less than the numerator.


# The raise statement allows the programmer to force a specific exception to occur. 
# The sole argument in raise indicates the exception to be raised. 
# This must be either an exception instance or an exception class (a class that derives from Exception).


def division(num1=0, num2=0):
    c = 0
    try:
        # raise exception if denominator is less than the numerator.
        if int(num2) > int(num1):
            raise Exception("Denominator should not be less than Numerator.")   
        
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
