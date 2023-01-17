#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input a number  from user and print number of 
#                                                digits present in that number.
#

# Take input as integer from user
num = int(input("Input a number:"))

# Convert that number to string and then print the length of string as number of digits.
num_of_digits = len(str(num))

# Print results.
print("Number of digits in", num, ":", num_of_digits)