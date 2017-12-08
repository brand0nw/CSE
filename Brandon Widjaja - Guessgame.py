import random


print("Guess a number between 0-50.")
print("You have 5 tries.")
print("Have fun.")
num = random.randint(0, 50)
# print(num)


# print(guess == str(num))
for x in range(5):
    guess = input("What is your guess? ")

    if guess == str(num):
        print("Correct. Good job!")
        quit()
    elif guess >= str(num):
        print("Lower")
    elif guess <= str(num):
        print("Higher")

print("Press enter to see answer.")
print("This is the right number.")
print(num)
quit()

# 1. Generate random number
# 2. Take an input(number) from the user
# 3. Compare input to generated number
# 4. Add "Higher" and "Lower" statements
# 5. Add 5 guesses
