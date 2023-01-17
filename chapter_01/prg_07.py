#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input width and height of rectangle from user 
#                                                and calculate area and perimeter of rectangle. 
#

w = float(input("Input width of rectangle:"))
l = float(input("Input height of rectangle:"))

# Calculate area of rectangle
area = w*l

# Calculate perimeter of rectangle
p = 2 * ( l + w )

# Print results.
print("Area of rectangle: ", area)
print("Perimeter of rectangle: ", p)