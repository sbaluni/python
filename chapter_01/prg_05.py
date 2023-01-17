#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input 2 numbers from user and perform swapping operation.
#

a = float(input("Input a:"))
b = float(input("Input b:"))

# Swap value of a and b
c = a
a = b
b = c

# Print results.
print("----After swapping----")
print("Value of a:", a)
print("Value of b:", b)