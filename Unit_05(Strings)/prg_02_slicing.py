#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   --------------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        22/10/2023           Using slicing operator explore different scenarios possible with slicing.

my_str = "HELLO PYTHON"
print(f"String:{my_str}")
print("String:", my_str[0:], sep="")

# Extract first 2 characters from string. We can use slicing operator like this [start_index : end_index] where
# end_index is not inclusive.
print("First 2 characters of string:", my_str[0:2])


# Extract substring from 3rd character to 7th character.
# 3rd character means index 2. 
# 7th character means index 6.
# Therefore we can use [2:7] because end_index in not inclusive.
print("Substring from 3rd character to 7th character:", my_str[2:7])

# Print substring from 4th character to end of string.
print("Substring from 4th character to end of string:", my_str[3:])

# Print substring from 7th character to end of string using negative index.
print("Substring from 7th character to end of string", my_str[-6:])

# Print substring "YTH" from my_str using negative index.
# Negative index of Y is -5
# Negative index of H is -3. Since end_index is not inclusive, so we have to use -2 to extract YTH
print("Substring:", my_str[-5:-2])
