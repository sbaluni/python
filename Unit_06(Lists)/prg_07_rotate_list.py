#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        09/04/2025           Given an array arr[]. Rotate the array to the left 
#                                                (counter-clockwise direction) by d steps, where d is 
#                                                a positive integer. 
# Example:
# Input: arr[] = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]

# Method 1: Using a temp list and slicing operation on list
def rotate_list1(arr, d):
    # Re-calculate d for the cases when value of d is greater than length of arr.
    d = d%len(arr)
    # Create a temp list and add elements from dth position to last element of array.
    # then add first d element at end of temp list to get final rotated list.
    temp_arr = arr[d:] + arr[0:d]
    # Return the final list
    return temp_arr

# Define list of integers
arr = [1, 2, 3, 4, 5]
# Take number of rotation as input from user.
d = int(input("Number of rotation:"))

arr = rotate_list1(arr, d)

print(f"List after {d} rotations:{arr}")