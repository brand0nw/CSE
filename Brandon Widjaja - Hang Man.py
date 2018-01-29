import random
import string
"""
A general guide for Hangman
1. Make a word bank - 10 items - good
2. Pick a random item from the list - done
3. Add a guess to the list of letters guessed - done
4. Reveal letters already guessed - done
5. Create the win condition - done i think?
"""

print("Welcome to Hangman.")
word_bank = ["Hot!", "Cheese.", "Charlie?", "Daniels?", "Kenshiro?", "Edison!", "Georgia.",
             "liberty!", "Nani.", "Computer?"]
guesses_left = 10

word = random.choice(word_bank)

letters_guessed = list(string.punctuation + " ")
player_guess = "True"

listTwo = list(letters_guessed)

punctuation = string.punctuation
print("You have 10 guesses.")

while word != player_guess:
    # Build output
    output = []
    for letter in word:
        if letter.lower() in letters_guessed:
            output.append(letter)

        else:
            output.append("*")

    print("".join(list(output)))

    if output == list(word):
        print("".join(list(word)))
        print("You Win!")
        print("Game Over")
        exit(0)

    # Ask for input
    current_guess = input().lower()

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
    print("You've guessed %s." % ", ".join(list(letters_guessed)))
