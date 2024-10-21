#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   -------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Input two numbers and calculate HCF(Highest Common Factor)

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
hcf = 1
small_num = num1 if num1 < num2 else num2

for i in range(small_num, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
        break

print(f"HCF of {num1} and {num2} is {hcf}")