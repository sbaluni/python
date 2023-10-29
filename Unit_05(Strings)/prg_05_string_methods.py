#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------
#   Suryakant Baluni        25/10/2023           Explore various string methods.

s = input("Enter a string:")

# capitalize : Upper case the first letter, lower case rest of string.
print("capitalize:", s.capitalize())

# lower : Make the string lower case.
print("lower:", s.lower())

# casefold: Make the string lower case.
# It is similar to the lower() method, but the casefold() method converts more characters into lower case.
# For example, the German lowercase letter 'ß' is equivalent to 'ss'. 
# Since it is already lowercase, the lower() method would not convert it; 
# whereas the casefold() converts it to 'ss'. 
print("casefold:", s.casefold())

# upper : Make the string upper case.
print("upper:", s.upper())

# swapcase : Make the lower case letters upper case and the upper case letters lower case:
print("swapcase:", s.swapcase())

# title : Make the first letter in each word upper case.
print("title:", s.title())

# count : Return the number of times the substring appears in the string.
print("How many times substring 'python' is present:", s.count("python"))
print("How many times substring 'python' is present from 3rd to 20th position:", s.count("python", 3, 20))