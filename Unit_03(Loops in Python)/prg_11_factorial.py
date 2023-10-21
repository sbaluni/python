#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Write a program to calculate factorial of a input number.

num = int(input("Enter number:"))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")