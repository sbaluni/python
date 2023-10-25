#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------
#   Suryakant Baluni        22/10/2023           Take a string as input from user, and traverse 
#                                                each of it's element using for loop.

my_str = input("Enter a string:")
counter = 0
for i in my_str:
    print(f"my_str[{counter}] : {i}")
    counter += 1