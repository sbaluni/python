#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   -----------------------------------------------------------------------------------------------------------------
#   Suryakant Baluni        05/07/2025           Randomly generate a number between 1-10.
#                                                Ask user to guess the number.
#                                                Give user 5 attempts to guess the number.
#                                                If user guesses correct number then print "You win!!!" and exit program.
#                                                If all 5 attempts failed then print "You lose."
#                                                When user's guess is wrong then give user a hint that 
#                                                the gussed number is less than/greater than the answer.

import random
rand_num = random.randint(1, 10)
#print(rand_num)
for i in range(1,6):
    print(f"[{i}/5 Attempt]: ", end ="")
    choice = int(input("Guess the number(1-10):"))
    if choice == rand_num:
        print("You win!!!")
        break
    elif choice < rand_num:
        print(f"Wrong answer. {choice} is smaller than the actual answer. Please try again.")
    else:
        print(f"Wrong answer. {choice} is greater than the actual answer. Please try again.")
else:
    print(f"You lose. Correct answer is {rand_num}")

