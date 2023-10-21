#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Take a number as input from user and identify if the 
#                                                number is prime or not.

import math

num = int(input("Enter a number:"))

if num > 1:
    num_sqrt = int(math.sqrt(num))
    for i in range(2, num_sqrt + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break;
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")