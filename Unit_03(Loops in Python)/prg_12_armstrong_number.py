#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Write a program to check whether a given number is 
#                                                an Armstrong number or not.
#
#   When the sum of the cube of the individual digits of a number is equal to that number, 
#   the number is called Armstrong number. 
#   For Example 153 is an Armstrong number because 153 = 13+53+33.

num = int(input("Enter number:"))
temp = num
s = 0
while temp > 0:
    rem = temp % 10
    s += rem ** 3
    temp = int(temp / 10)

if num == s:
    print(f"{num} is Armstrong.")
else:
    print(f"{num} is not Armstrong.")