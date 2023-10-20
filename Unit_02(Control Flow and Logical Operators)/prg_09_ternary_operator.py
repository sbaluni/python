#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input a number from user and check if the 
#                                                number is even or odd. Use ternary operator.
#
#   Syntax:  <Expression_on_True> if <Condition> else <Expression_on_False>

num = int(input("Input a number:"))

print("%d is Even." % num) if num % 2 == 0 else print("%d is Odd." % num)