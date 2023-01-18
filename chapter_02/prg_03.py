#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------
#   Suryakant Baluni        18/01/2023           Take height and weight as input from user and calculate BMI.
#                                                Formula to calculate BMI = weight/(height*height).
#                                                Based on BMI display following information to user:
#                                                -> If BMI is under 19 they are underweight
#                                                -> Over 19 but below 25 they have a normal weight
#                                                -> Over 25 but below 30 they are slightly overweight
#                                                -> Over 30 but below 35 they are obese
#                                                -> Above 35 they are clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round( weight / (height ** 2) )

if bmi < 19:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 19 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")