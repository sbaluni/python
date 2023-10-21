#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   --------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Write a script that generates a random flaoting
#                                                point number between 1-100.

import random

# random.random generates a float between 0-1.
rand_float = random.random()

# Therefore in order to get random number between 1-100, we can multiply the output by 100
rand_float = rand_float * 100

print(rand_float)