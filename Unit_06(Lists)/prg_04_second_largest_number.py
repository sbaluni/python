#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        08/04/2025           Given an array of positive integers, return the 
#                                                second largest element from the array. 

# Define list of integers
arr = [23, 200, 43, 12, 22, 100, 67, 300, 4000]

# Assume largest and second largest number in array are Negative Infinity (the smallest number possible)
largest_num = float('-inf')
sec_largest_num = float('inf')

for num in arr:
    
    if num > largest_num:
        sec_largest_num = largest_num
        largest_num = num
    elif num > sec_largest_num and num != largest_num:
        sec_largest_num = num

print("Second Largest number in array is:", sec_largest_num)
