#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Take a number as input from user and identify if the
#                                                number is palindrom or not.

num = int(input("Enter a number:"))

# Convert integer to string and then reverse the string
rev_num = int(str(num)[::-1])
print(f"Reverse Of Number: {rev_num}")

print(f"{num} is Palindrom.") if num == rev_num else print(f"{num} is not Palindrom.")