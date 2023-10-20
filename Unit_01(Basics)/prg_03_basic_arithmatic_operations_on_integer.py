#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input 2 integers from user and perform basic 
#                                                arithmatic operations.
#

# input() function is used to take input from user. It returns a string.
# So in order to perform numeric operations on variables we need to convert input to int type first using int().
a = int(input("Input a(int):"))
b = int(input("Input b(int):"))

# Perform various arithmatic operations and store results in individual variables.
sum = a + b
diff = a - b
multi = a*b
division = a/b              # Returns float
floor_division = a//b       # Returns int
rem = a % b
power = a ** b

# Print results.
print("Sum:", sum)
print("Difference:", diff)
print("Multiplication:", multi)
print("Division:", division)
print("Floor Division:", floor_division)
print("Remainder:", rem)
print(a, " to power ", b, " is: ", power)