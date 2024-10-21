#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ----------------------------------------------------------------------------------------------------
#   Suryakant Baluni        30/10/2023           Develop Rock, Paper, Scissor game based on below rules.
#                                                Take user's choice as input from user, and generate 
#                                                computer's choice randomly.
#
#   Game Rules:
#       1. Rock wins against scissors.
#       2. Scissors win against paper.
#       3. Paper wins against rock.

import random

game_rules = '''\nGame Rules:
       1. Rock wins against scissors.
       2. Scissors win against paper.
       3. Paper wins against rock.\n'''

print(game_rules)
# Take user choice as input from user.
user_choice = input("Type 0 for Rock, 1 for Paper or 2 for Scissors:")

# Valid choices.
valid_choices = "012"

# Validate user choice
if user_choice in valid_choices:
    
    # If user choice is valid, then randomly generate computer's choice
    computer_choice = str(random.randint(0, 3))
    
    print(f"Computer's choice: {computer_choice}")
    
    if user_choice == "0" and computer_choice == "2": 
        print("You Win!!")
    elif user_choice == "1" and computer_choice == "0":
        print("You Win!!")
    elif user_choice == "2" and computer_choice == "1":
        print("You Win!!")
    elif user_choice == computer_choice:
        print("It's a tie!!")
    else:
        print("You Lose!!")
else:
    print("Invalid choice!!!")