#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input 2 floating numbers from user and perform basic arithmatic operations.
#

a = float(input("Input number a:"))
b = float(input("Input number b:"))

# Perform various arithmatic operations and store results in individual variables.
sum = a + b
diff = a - b
multi = a*b
division = a/b
rem = a % b

# Print results.
print("Sum:", sum)
print("Difference:", diff)
print("Multiplication:", multi)
print("Division:", division)
print("Remainder:", rem)