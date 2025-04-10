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

def rotate_list1(arr, d):
    # Re-calculate d for the cases when value of d is greater than length of arr.
    d = d%len(arr)
    # Store the elements from dth position to end of array to a temp list
    temp_arr = arr[d:]
    # Append first d elements from arr to temp array
    temp_arr[len(temp_arr):] = arr[0:d]
    # Copy entire temp list to arr
    arr[:] = temp_arr[:]


# Define list of integers
arr = [1, 2, 3, 4, 5]
# Take number of rotation as input from user.
d = int(input("Number of rotation:"))

rotate_list1(arr, d)

print(f"List after {d} rotations:{arr}")