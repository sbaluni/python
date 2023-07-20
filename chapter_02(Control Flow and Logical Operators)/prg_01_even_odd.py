#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input a number from user and check if the 
#                                                number is even or odd.

num = int(input("Input a number:"))

if num % 2 == 0:
    print("%d is Even." % num)
else:
    print("%d is Odd." % num)