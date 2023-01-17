#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input 2 numbers from user and calculate sum of those 2 numbers.
#

# input() function is used to take input from user. It returns a string.
# So in order to perform numeric operations on variables we need to convert input to int type first using int().
a = int(input("Input a:"))
b = int(input("Input b:"))

# Calculate sum and store result in a variable c
c = a + b

# Print sum of a and b.
print("Sum:", c)