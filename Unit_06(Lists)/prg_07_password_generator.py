#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/11/2023           Ask user for number of letters, numbers and symbols
#                                                as input, and generate a random password based on 
#                                                inputs.
#
#   Sample Input:
#       Enter number of letters:2
#       Enter number of numbers:3
#       Enter number of Symbols:3
#
#   Sample output:
#       Generated password: G$3#94*a

import random as r

print("\n\n=============== P A S S W O R D  G E N E R A T O R ===============\n")

# Take inputs from user.
num_letters = int(input("Enter number of letters:"))
num_numbers = int(input("Enter number of numbers:"))
num_symbols = int(input("Enter number of symbols:"))

# Define metadata
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '~', '!', ':', ';', '?']


# Variables to store final generated password.
gen_passwd = ""
passwd_list = []

# Generate random letters    
for i in range(0, num_letters):
    get_rand = r.choice(letters)
    letters.remove(get_rand)
    # This if block is to make sure we have combination of lower and UPPER case letters.
    if i % 2 == 0:
        get_rand = get_rand.upper()
    passwd_list.append(get_rand)
    
# Generate random numbers
for i in range(0, num_numbers):
    get_rand = r.choice(numbers)
    numbers.remove(get_rand)
    passwd_list.append(str(get_rand))

# Generate random symbols
for i in range(0, num_symbols):
    get_rand = r.choice(symbols)
    symbols.remove(get_rand)
    passwd_list.append(get_rand)

# Shuffle the order of generated password
r.shuffle(passwd_list)

gen_passwd = ''.join(passwd_list)

print(f'Generated password:{gen_passwd}')