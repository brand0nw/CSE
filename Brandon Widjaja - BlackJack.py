import random


print("Welcome to BlackJack the game of luck.")

rounds = 0
BlackJack = 21
money = 15

while money >= 0:

    money -= 1
    rounds += 1
    print("You have %s dollars." % money)
    card1 = random.randint(1, 10)
    card2 = random.randint(1, 10)
    value = card1 + card2

    print(value)

    if value == 21:
        print("You win.")
        input()
