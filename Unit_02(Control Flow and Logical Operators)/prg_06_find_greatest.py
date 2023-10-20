#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   -------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Take 3 numbers as input from user and find the
#                                                largest number.

num1 = int(input("Input first number:"))
num2 = int(input("Input second number:"))
num3 = int(input("Input third number:"))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is greatest")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is greatest")
elif num3 >= num1 and num3 >= num2:
    print(f"{num3} is greatest")
