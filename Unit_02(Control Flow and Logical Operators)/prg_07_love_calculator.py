#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   -------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Take name of two persons as input from user.
#                                                
#   Perform following calculation based on input names.
#   1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
#   2. Then check for the number of times the letters in the word LOVE occurs. 
#   3. Then combine these numbers to make a 2 digit number.
#
#   For Love Scores less than 10 or greater than 90, the message should be:
#   "Your score is *x*, you go together like coke and mentos."
#
#   For Love Scores between 40 and 50, the message should be:
#   "Your score is *y*, you are alright together."
#
#   Otherwise, the message will just be their score. e.g.:
#   "Your score is *z*."



name1 = input("First Name:")
name2 = input("Second Name:")

combined_name = name1.upper() + name2.upper()

true_score = combined_name.count("T") + combined_name.count("R") + combined_name.count("U") + combined_name.count("E")
love_score = combined_name.count("L") + combined_name.count("O") + combined_name.count("V") + combined_name.count("E")
final_score = int(str(true_score) + str(love_score))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")