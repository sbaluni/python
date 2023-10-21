#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   -----------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Print even numbers between 1-10 using for loop.
#                                                

# in range function we can specify the start, stop and step
# In this case start with 2, stop at 10 and increment by 2 each time. 
for i in range(2, 11, 2):
    print(i)


print("------------Method 2 (Using for loop and if statement)-------------------")
for i in range(1,11):
    if i % 2 == 0:
        print(i)