#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input radius of circle from user and calculate 
#                                                area and perimeter of circle. 
#

r = float(input("Input radius of circle:"))

# Define value of pi
pi = 3.14

# Calculate area of rectangle
area = pi * r * r

# Calculate perimeter of rectangle
p = 2 * pi * r

# Print results.
print("Area of circle: ", area)
print("Perimeter of circle: ", p)