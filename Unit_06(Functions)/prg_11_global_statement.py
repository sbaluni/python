#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        07/08/2025           Demonstrate global statement: Modify a global variable 
#                                                from within a function.


# Statement 'global var1' at top of this function tells Python that var1 refers to the global variable.
# So don’t create a local variable with this name.
def set_values():
    # This should always be first line of function.
    global var1
    var1 = 'Local var1 set_values'
    print("Value of var1 inside set_values:", var1)


# This var1 is global variable and has global scope.
var1 = 'Global var1'
print("Value of var1[before set_values]:", var1)
set_values()
print("Value of var1[after set_values]:", var1)