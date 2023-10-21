#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   -----------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Print even numbers between 1-10 using while loop.
#                                                When while loop finishes successfully, then print "Loop finished."

# When else is used with while loop, note that else block will be executed when while loop finishes all it's 
# iterations. If loop is explicitly exited using break statement then else block will not be executed.
i = 2
while i <= 10:
    print(i)
    i += 2
else:
    print("Loop finished.")