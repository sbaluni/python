#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        08/04/2025           Given an array of positive integers, move all the zeros
#                                                to the right end while maintaining the relative order of 
#                                                the non-zero elements.
# Example:
# Input: arr[] = [1, 5, 0, 2, 3, 0, 5, 0]
# Output: [1, 5, 2, 3, 5, 0, 0, 0]

# Define list of integers
arr = [1, 5, 0, 2, 3, 0, 5, 0]

count = 0

for i in range(0, len(arr)):
    if arr[i] != 0:
        arr[i], arr[count] = arr[count], arr[i]
        count += 1

print("Modified Array is:", arr)