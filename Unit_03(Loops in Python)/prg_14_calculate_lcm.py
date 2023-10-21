#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   -------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Input two numbers and calculate LCM(Least Common Multiple)

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
lcm = 1
max_num = num1 if num1 > num2 else num2

i = max_num
while lcm == 1:
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break
    i += max_num

print(f"LCM of {num1} and {num2} is {lcm}")