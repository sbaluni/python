#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Take a number as input from user and display table of 
#                                                that number in below format.
#
#   3 X 1 = 3
#   3 X 2 = 6
#   3 X 3 = 9
#   .........
#   .........
#   3 X 10 = 30
#                                                

num = int(input("Enter a number:"))

for i in range(1,11):
    product = num * i
    print(f"{num} X {i} = {product}")