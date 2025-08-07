#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        07/08/2025           Demonstrate global and local scope of variables.


# This function has local variable var1. Therefore it will use local value of var1 in this  function's scope.
def set_values():
    var1 = 'Local var1 set_values'
    print("Value of var1 inside set_values:", var1)

# Since print_values doesn't have local variable var1, so it will access glabal variable var1.
def print_values():
    print("Value of var1 inside print_values:", var1)

# This var1 is global variable and has global scope
var1 = 'Global var1'
print_values()
set_values()
print("Value of var1[after set_values]:", var1)