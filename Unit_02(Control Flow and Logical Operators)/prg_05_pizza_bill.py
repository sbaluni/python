#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Take following 3 inputs from user:
#                                                1. Pizza size: (S | M | L)
#                                                2. Add pepperoni: (Y | N)
#                                                3. Add extra cheese: (Y | N)
#
#   Based on above inputs calculate the final bill of customer. Assume the prices as below.
#   Small pizza (S): $15
#   Medium pizza (M): $20
#   Large pizza (L): $25
#
#   Add pepperoni for small pizza: +$2
#   Add pepperoni for medium or large pizza: +$3
#
#   Add extra cheese for any size pizza: +$1

# Converting user input to upper case so that user can input either lower case or upper case.
size = input("Please input pizza size(S|M|L)?").upper()
pepperoni = input("Would you like to add pepperoni(Y/N)?").upper()
extra_cheese = input("Would you like to add extra cheese(Y/N)?").upper()

total_bill = 0
if size == "L":
    total_bill = 25
elif size == "M":
    total_bill = 20
else:
    total_bill = 15

if pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

if extra_cheese == "Y":
    total_bill += 1

print(f"Your final bill is:{total_bill}")