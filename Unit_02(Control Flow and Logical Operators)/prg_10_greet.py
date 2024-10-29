#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        29/10/2024           Greet user differently based on current time.
#

import time

name = input('What is your name?:').capitalize()
hour = int(time.strftime('%H'))

if hour >= 4 and hour < 12:
    print(f'Good Morning {name}!!!')
elif hour >= 12 and hour <17:
    print(f'Good Afternoon {name}!!!')
elif hour >= 17 and hour < 21:
    print(f'Good Evening {name}!!!')
else:
    print(f'Good Night {name}!!!')