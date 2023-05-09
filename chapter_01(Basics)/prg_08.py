#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        17/01/2023           Input radius of circle from user and calculate 
#                                                area and perimeter of circle up to 2 decimal places. 
#

r = float(input("Input radius of circle:"))

# Define value of pi
pi = 3.14

# Calculate area of circle
area = pi * r * r

# Calculate perimeter of circle
p = 2 * pi * r

# Print results. Use formatting options to format output up to 2 decimal places.
# This is useful when output is something like 3.1, but we want to print 3.10
print("Area of circle: %.2f" % area)
print("Perimeter of circle: %.2f" % p)

# We can also use formatting syntax like this.
print("Area of circle: " + "{:.2f}".format(area))
print("Perimeter of circle: " +  "{:.2f}".format(p))