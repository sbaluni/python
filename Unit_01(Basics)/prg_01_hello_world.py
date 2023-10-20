#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------
#   Suryakant Baluni        02/08/2022           Python program to use print function.
#

# Print "Hello, world!"". We can use either single or double quotes.
print("Hello, world!")
print('Hello, world again!')

# Print single quoted string. If we use double quotes then no need to escape single quote by \
print("'I am single quoted string'")
print('\'I am single quoted string\'')

# Double quoted string. If we use single quotes then no need to escape double quote by \
print('"I am double quoted string"')
print("\"I am double quoted string\"")

# Print text in new line using \n
print("Hello there,\nHow are you?")

# Here \n is treated as new line.
print('C:\some\name')

# If we don't want characters prefaced by \ to be interpreted as special characters
# then use raw string by adding r before first quote
print(r'C:\some\name')

# Print more than one string. This will print "Hello world!". Note that default separator is space.
print("Hello", "world!")

# Print more than one string with separator as comma.
# This statement will display "Hello,Python,world!"
print("Hello", "Python", "world!", sep=",")

# Print more than one string with separator as comma. Also use string END_OF_LINE instead of \n as default line break.
# This statement will print "Hello,Python,world!END_OF_LINE". See at the end of string END_OF_LINE is appended instead of \n.
print("Hello", "Python", "world!", sep=",", end="END_OF_LINE")