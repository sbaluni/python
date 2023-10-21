#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Take a number as input from user and print reverse 
#                                                of that number.

num = int(input("Enter a number:"))

rev_num = 0
while num > 0:
    rem = num % 10
    rev_num = rev_num * 10 + rem
    num = int(num / 10)

print(f"Reverse Of number: {rev_num}")


print("\n\n------------Method 2(Using string concept)--------------------")
num = int(input("Enter a number:"))

# Convert integer to string and then reverse the string
num = str(num)
rev_num = int(num[::-1])
print(f"Reverse Of Number: {rev_num}")