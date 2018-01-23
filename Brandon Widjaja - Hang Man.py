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
print(len(word_bank))
print(word_bank)
print(word)
letters_guessed = []
player_guess = "True"
while word != player_guess:
    output = []
    guess = input()
    if guess == 'quit':
        exit(0)
    letters_guessed.append(guess)
    letter = string.ascii_lowercase
    print(letters_guessed)
    print(output)

    if letter == guess:

        output.append(guess)
    # if guess != letter:
    #     guesses_left -= 1
    #     print("%s guesses left." % guesses_left)
    #
    # if guess = letter:
    #     print()
