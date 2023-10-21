#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Write a program to calculate sum of first N natural numbers.

n = int(input("Enter N:"))
s = 0
for i in range(1, n + 1):
    s += i
print(f"Sum of first {n} natural number:{s}")


print("\n-----------Method 2 (Using direct formula)-------------")
s = n*(n+1)/2
print(f"Sum of first {n} natural number:{s}")
