#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   --------------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        22/10/2023           Define a string and display each of it's characters by specifying index.

my_str = "HELLO"

# In Python string indexes starts from 0. my_str[0] prints H
print("1st characters is:", my_str[0])
print("2nd characters is:", my_str[1])
print("3rd characters is:", my_str[2])
print("4th characters is:", my_str[3])
print("5th characters is:", my_str[4])

# Below print will give error because index 5 doesn't exists.
# IndexError: string index out of range
# print("5th characters is:", my_str[5])

# Python also supports negative indexing. That means index -1 represents the last element of string.
# Index -2 represents 2nd last element of string, and so on...
print("\n-------------Using negative indexing-------------")
print("5th characters is:", my_str[-1])
print("4th characters is:", my_str[-2])
print("3rd characters is:", my_str[-3])
print("2nd characters is:", my_str[-4])
print("1st characters is:", my_str[-5])

