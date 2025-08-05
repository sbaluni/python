#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   -----------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/10/2023           Randomly generate a number between 1-10.
#                                                Ask user to guess the number.
#                                                Give user 3 attempts to guess the number.
#                                                If user guesses correct number then print "You win!!!" and exit program.
#                                                If all 3 attempts failed then print "You lose."

import random
rand_num = random.randint(1, 10)
#print(rand_num)
for i in range(1,4):
    choice = int(input("Guess the number(1-10):"))
    if choice == rand_num:
        print("You win!!!")
        break
    else:
        print("Wrong answer. Please try again.")
else:
    print(f"You lose. Correct answer is {rand_num}")

