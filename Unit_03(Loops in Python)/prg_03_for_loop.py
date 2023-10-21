#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   -----------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Print numbers between 1-10 using for loop.
#                                                When for loop finishes successfully, then print "Loop finished."

# When else is used with for loop, note that else block will be executed when for loop finishes all it's 
# iterations. If loop is explicitly exited using break statement then else block will not be executed.

for i in range(1, 11):
    print(i)
else:
    print("Loop finished.")