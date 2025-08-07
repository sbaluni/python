#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        07/08/2025           Demonstrate local scope of variables.


# Both the print will display value of var1 as 'Local var1 set_values'.
def set_values():
    var1 = 'Local var1 set_values'
    print("Value of var1 inside set_values[before calling override_values]:", var1)
    override_values()
    print("Value of var1 inside set_values[after calling override_values]:", var1)


def override_values():
    # This var1 is differend from the var1 variable in set_values
    # This var1 here has scope limited to override_values function only.
    var1 = 'Local var1 override_values'
    print("Value of var1 inside override_values:", var1)

    # var2 is local variable of override_values. And it can't be accessed outside override_values().
    var2 = 'Local var2 override_values' 
    
set_values()