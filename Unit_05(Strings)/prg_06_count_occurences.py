#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------
#   Suryakant Baluni        09/11/2023           Take 2 strings as input from user(string and a substring).
#                                                You have to print the number of times the substring 
#                                                occurs in the given string. 
#
#   Sample Input:
#       Enter string: ABCDCDC
#       Enter sub string: CDC
#
#   Sample output:
#       CDC present 2 time in ABCDCDC

string = input("Enter string:")
sub_string = input("Enter sub string:")

cnt = 0
len_string = len(string)
len_sub_string = len(sub_string)

# Traverse string from starting index to the index a substring of length of sub_string can be extracted 
for i in range(0, len_string - len_sub_string + 1):
        # Extract the substring of length equal to sub_string from current index
        # and compare it with the sub string provided by user.
        # If matches, increase the counter by 1
        if string[i:len_sub_string + i] == sub_string:
            cnt += 1

print(f"{sub_string} present {cnt} time in {string}")