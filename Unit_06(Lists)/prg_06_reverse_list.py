#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        08/04/2025           Given an array of integers, reverse the element of list.
#   
# Example:
# Input: arr[] = [1, 5, 0, 2, 3, 0, 5, 0]
# Output: [0 ,5, 0, 3, 2, 0, 5, 1]

# Method 1: Using slicing
def reverse_list1(arr):
    arr[:] = arr[::-1]

# Method 2: Using inbuilt list method
def reverse_list2(arr):
    arr.reverse()

# Method 3: Without using any inbuilt methods
def reverse_list3(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i+1, j-1

# Define list of integers
arr = [1, 5, 0, 2, 3, 0, 5, 0]
reverse_list3(arr)

print("Reversed list:", arr)