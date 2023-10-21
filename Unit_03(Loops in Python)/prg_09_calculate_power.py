#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Take two numbers "num" and "power" as input and 
#                                                calculate num^power. Don't use any library function or ** operator.

num = int(input("Enter number:"))
power = int(input("Enter power:"))

p = 1
for i in range(1, power + 1):
    p *= num

print(f"{num} to power {power} is {p}")