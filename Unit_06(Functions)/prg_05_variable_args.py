#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        05/08/2025           Write a python function that accepts any number of integer
#                                                arguments and returns sum of all the arguments.

# The asterisk in the parameter name *p_numbers tells Python to make a tuple called p_numbers, 
# containing all the values this function receives. 
def addition(*p_numbers):
    return sum(p_numbers)


s = addition(1,2,3)
print("Sum:", s)

s = addition(1,2,3,4,5)
print("Sum:", s)