#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        18/01/2023           Take year as input from user and print if the
#                                                year is a leap year or not.

year = int(input("Please enter year(YYYY): "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is leap year.")
else:
    print(f"{year} is not a leap year.")