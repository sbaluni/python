#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        13/10/2025           Write a function named collatz() that has one parameter named number. If
#                                                number is even, then collatz() should print number // 2 and return this value.
#                                                If number is odd, then collatz() should print and return 3 * number + 1.
#                                                Then write a program that lets the user type in an integer and that keeps
#                                                calling collatz() on that number until the function returns the value 1.
#
#                                                Add Validation: Add try and except statements to detect whether the
#                                                user types in a noninteger string. if user has given input as any noninteger string, 
#                                                then print a message to the user saying they must enter an integer.

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        raise ValueError("The number must be a positive integer.")
    
    while num != 1:
        num = collatz(num)
        print(num)
    
except ValueError:
    print("Invalid input. Please enter a positive integer.")
