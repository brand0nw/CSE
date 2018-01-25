import random
import string

"""
A general guide for Hangman
1. Make a word bank - 10 items - good
2. Pick a random item from the list - done
3. Add a guess to the list of letters guessed - done
4. Reveal letters already guessed - done
5. Create the win condition - working
"""

print("Welcome to Hangman.")
word_bank = ["hot", "cheese", "Charlie", "Daniels", "Kenshiro", "Edison", "Georgia", "liberty", "trombone", "computer"]
guesses_left = 10

word = random.choice(word_bank)

letters_guessed = []
player_guess = "True"

print("You have 10 guesses.")

while word != player_guess:
    # Build output
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)

        else:
            output.append("*")
    print(output)

    if output == list(word):
        print("".join(list(word)))
        print("You Win!")
        print("Game Over")
        exit(0)

    # Ask for input
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


