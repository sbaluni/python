#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   -----------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Randomly generate a number between 0-1.
#                                                If generated number is 1 - print Heads else Tails.

import random
rand_num = random.randint(0, 1)
print("Heads") if rand_num == 1 else print("Tails")
