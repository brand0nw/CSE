import random
import string

"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed
5. Create the win condition
"""

print("Welcome to Hangman.")
the_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
word_bank = ["hot", "cheese", "charlie", "daniels", "kenshiro", "edison", "georgia", "liberty", "trombone", "computer"]
guesses_left = 10

word = random.choice(word_bank)

letters_guessed = []
player_guess = "True"

print("You have 10 guesses.")

while word != player_guess:

    output = []

    for letter in word:
        if letter in letters_guessed:
            output.append(letter)

        else:
            output.append("*")
    print(output)

    current_guess = input()

    if current_guess == 'quit':
        print("Game Over")
        exit(0)

    if current_guess not in word:
        guesses_left -= 1
        print("%s guesses left." % guesses_left)

    if guesses_left == 0:
        print("Game Over")
        exit(0)

    letters_guessed.append(current_guess)

    print(letters_guessed)

    if output == :
        print("You Win!")
        print("Game Over")
        exit(0)
