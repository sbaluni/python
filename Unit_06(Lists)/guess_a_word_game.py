#!/usr/bin/env python3
#
#   User                    Date(dd/mm/yyyy)     Description 
#   ------------------------------------------------------------------------------------------------
#   Suryakant Baluni        21/11/2023           Generate a random word and then
#                                                ask user to guess each letter of
#                                                the word. Each time user guesses
#                                                wrong letter take a life from user.
#                                                User wins if user guesses all letters correctly.
#                                                User lose if user guesses 6 wrong letters.
#
import random as r

# Prepare list of words to guess
words = ['APPLE', 'BANANA', 'CAT', 'DOG', 'PYTHON', 
         'JAVA', 'COMPUTER', 'SCIENCE', 'TECHNOLOGY',
         'KEYBOARD', 'LAPTOP', 'MIRROR', 'LEARN',
         'MOBILE', 'HUMAN', 'MOVIE', 'HOLIDAY']

# Choose a random word from list
gen_word = r.choice(words)
#print("Choosen word:", gen_word)

# Generate a masked string to hide actual letters from user.
masked_gen_word = '_ ' * len(gen_word)
masked_gen_word = masked_gen_word.strip().split(' ')
print("Guess the letters present for each underscore :", ' '.join(masked_gen_word))

# Set number of lives.
lives = 6
end_of_game = False

# Play the game until end of game(Either user wins or lose)
while not end_of_game:
    user_choice = input('\n\nGuess a letter:').upper()
    
    # Already guessed
    if user_choice in masked_gen_word:
        print("You have already guessed ", user_choice)
    
    # Check if the guessed letter is present.
    # If yes then fill that letter in masked_gen_word
    for i in range(len(gen_word)):
        if user_choice == gen_word[i]:
            masked_gen_word[i] = user_choice
    
    # Take a life back if user choice is wrong
    if user_choice not in gen_word:
        lives -= 1
        print("Wrong guess!!! Your Remaining lives:", lives)
    
    print("Word after your guesses:", ' '.join(masked_gen_word))
    
    # User gussed all letters
    if '_' not in masked_gen_word:
        print("!!!!!!! C o n g r a t u l a t i o n s    Y o u    W i n !!!!!!!")
        end_of_game = True
    
    # User lost all life lines
    if lives <= 0:
        print("!!!!!!! Y o u   L o s e !!!!!!!")
        end_of_game = True