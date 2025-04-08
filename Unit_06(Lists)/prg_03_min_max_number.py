#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        08/04/2025           Given an array of positive integers, return the 
#                                                largest and smallest element from the array. 

# Define list of integers
arr = [23, 200, 43, 12, 22, 100, 67, 300]

# Assume largest number in array is Negative Infinity (the smallest number possible)
largest_num = float('-inf')

# Assume smallest number in array is Positive Infinity (the largest number possible)
smallest_num = float('inf')

# Get largest and smallest number by traversing list
for num in arr:
    # Code block to get largest number.
    if num > largest_num:
        largest_num = num
    
    # Code block to get smallest number.
    if num < smallest_num:
        smallest_num = num

print("Largest number in array is:", largest_num)
print("Smallest number in array is:", smallest_num)