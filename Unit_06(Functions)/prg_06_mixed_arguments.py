#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        05/08/2025           Write a python function that accepts size of pizza as first
#                                                argument, and an arbitrary argument *p_toppings as second parameter.
#                                                And then prints details about the pizza.

# p_size is positional argument.
# p_toppings is arbitrary argument
def make_pizza(p_size, *p_toppings):
    print(f'Making {p_size} pizza with following toppings:')
    for i in p_toppings:
        print(f'-- {i}')

make_pizza('Large', 'mushrooms', 'green peppers', 'extra cheese')

make_pizza('Regular', 'pepperoni')
