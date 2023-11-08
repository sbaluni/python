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
print("How many times substring 'python' is present between 3rd to 20th position:", s.count("python", 3, 20))

# startswith : Returns True if the string starts with the specified value, otherwise False.
print("Does string starts with 'on':", s.startswith('on'))
print("Does string present at 5 to 10 position starts with 'on':", s.startswith('on', 5, 10))

# endswith : Returns True if the string ends with the specified value, otherwise False.
print("Does string ends with 'on':", s.endswith('on'))
print("Does string present at 5 to 10 position ends with 'on':", s.endswith('on', 5, 10))

# find : find() method finds the first occurrence of the specified value.
# find() method returns -1 if the value is not found.
print("First occurance of 'Python' is present at index:", s.find('Python'))
print("First occurance of 'Python' between 5th to 15th index is present at index:", s.find('Python', 5, 15))

# The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
print("Last occurance of 'Python' is present at index:", s.rfind('Python'))
print("Last occurance of 'Python' between 5th to 15th index is present at index:", s.rfind('Python', 5, 15))


# index : index() method finds the first occurrence of the specified value.
# index() method raises an exception if the value is not found.
#print("First occurance of 'Python' is present at index:", s.index('Python'))
#print("First occurance of 'Python' between 5th to 15th index is present at index:", s.index('Python', 5, 15))


# rindex : rindex() method finds the last occurrence of the specified value.
# rindex() method raises an exception if the value is not found.
#print("Last occurance of 'Python' is present at index:", s.rindex('Python'))
#print("Last occurance of 'Python' between 5th to 15th index is present at index:", s.rindex('Python', 5, 15))


# isalnum: The isalnum() method returns True if all the characters are alphanumeric, 
# Meaning alphabet letter (a-z) and numbers (0-9).
# If any other character is present other than a-z and 0-9, isalnum return False
print("Is string alpha numeric:", s.isalnum())


# isalpha: The isalpha() method returns True if all the characters are alphabet letters (a-z).
print("Does string contains only alphabets:", s.isalpha())

# isascii: isascii() method returns True if all the characters are ascii characters
print("Does string contains only ascii characters:", s.isascii())

# isdecimal: isdecimal() method returns True if all the characters are decimals (0-9).
print("Does string contains only decimal characters:", s.isdecimal())

# isdigit: isdigit() method returns True if all the characters are digits, otherwise False.
print("Does string contains only digits:", s.isdigit())

# isidentifier: The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), 
# or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print("Is string a valid identifier:", s.isidentifier())

# islower() method returns True if all the characters are in lower case, otherwise False.
print("Is the string in lower case", s.islower())

# isupper() method returns True if all the characters are in upper case, otherwise False.
print("Is the string in upper case", s.isupper())

# isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
print("Are all characters of string are spaces:", s.isspace())

# istitle() method returns True if all words in a text start with a upper case letter, 
# AND the rest of the word are lower case letters, otherwise False.
print("Is string in title case:", s.istitle())


# lstrip() method removes any leading characters (space is the default leading character to remove)
print("Remove all the leading spaces from string:", s.lstrip())
print("Remove all the leading comma from string:", s.lstrip(','))

# rstrip() method removes any trailing characters (characters at the end a string), 
# space is the default trailing character to remove.
print("Remove all the trailing spaces from string:", s.rstrip())
print("Remove all the trailing comma from string:", s.rstrip(','))

# strip() method removes any leading, and trailing characters.
# space is the default trailing character to remove.
print("Remove all the leading and trailing spaces from string:", s.strip())
print("Remove all the leading and trailing comma from string:", s.strip(','))

# The partition() method searches for first occurrence of specified string, 
# and splits the string into a tuple containing three elements.
# -> The first element contains the part before the specified string.
# -> The second element contains the specified string.
# -> The third element contains the part after the string.
print("Partition the string by 'Python' substring:", s.partition('Python'))

# replace() method replaces a specified phrase with another specified phrase.
# Syntax: string.replace(oldvalue, newvalue, count) 
print("Replace all occurrences of 'Python' with 'Java': ", s.replace('Python', 'Java'))
print("Replace all only first 2 occurrences of 'Python' with 'Java': ", s.replace('Python', 'Java', 2))

# split() method splits a string into a list.
# default separator is any whitespace.
print("Split each word of string separated by space:", s.split())

# zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
print("zfill string to length 20:", s.zfill(20))