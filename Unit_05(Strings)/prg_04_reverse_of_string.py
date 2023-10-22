#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------
#   Suryakant Baluni        22/10/2023           Take a string as input from user, and print
#                                                reverse of that string.

my_str = input("Enter a string:")
rev_str = my_str[::-1]
print(f"Reverse of string[Method 1: Slicing]:{rev_str}")

# Without using slicing. Using While loop.
str_len = len(my_str) - 1
rev_str = ""
while str_len >= 0:
    rev_str += my_str[str_len]
    str_len -= 1

print(f"Reverse of string[Method 2: while loop]:{rev_str}")

# Using for loop
str_len = len(my_str) - 1
rev_str = ""
for i in range(str_len,-1,-1):
    rev_str += my_str[i]

print(f"Reverse of string[Method 3: for loop]:{rev_str}")
