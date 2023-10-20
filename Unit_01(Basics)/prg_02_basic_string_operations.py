#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Basic string manipulation.
#

# Concat 2 strings "Hello" and "Suryakant" using + or space.
# Note that space only works with literals, and not with variables or expressions.
print("Hello" + "Suryakant")
print("Hello"  " Suryakant." ' How are you?')


# Add a space between above 2 strings "Hello" and "Suryakant". 
# This can be done by any of below 3 ways.
print("Hello " + "Suryakant")
print("Hello" + " Suryakant")
print("Hello" + " " + "Suryakant")

# Here \n is treated as new line.
print('C:\some\name')

# If we don't want characters prefaced by \ to be interpreted as special characters
# then use raw string by adding r before first quote
print(r'C:\some\name')

# Multiline strings can be formed by triple quotes.
# Note that new line character is added automatically at end of each line.
print("""Hello Suryakant
How are you?""")
print('''Hello Suryakant
How are you?''')

# If we don't need new line in any of the lines, we can do that by adding a \ at end of that line.
print("""Hello Suryakant \
How are you?
Hey, I am fine.""")

# Repeat string multiple times using *
# For example if we want to print Hello 3 times.
print(3*"Hello ")
print("Hello "*3)

# Length of string using len() function.
print(len('Hello'))