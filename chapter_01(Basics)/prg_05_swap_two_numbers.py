#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input 2 numbers from user and perform 
#                                                swapping operation.
#

a = float(input("Input a:"))
b = float(input("Input b:"))

# Method 1: Swap value of a and b (Using third variable c)
# c = a
# a = b
# b = c

# Method 2: Swap value of a and b (Without using third variable)
# a = a + b
# b = a - b
# a = a - b

# Method 3: Swap value of a and b in single line
a, b = b, a

# Print results.
print("----After swapping----")
print("Value of a:", a)
print("Value of b:", b)