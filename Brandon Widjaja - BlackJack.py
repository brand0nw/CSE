import random


print("Welcome to BlackJack the game of luck.")

rounds = 0
BlackJack = 21
money = 15

while money >= 0:

    money -= 1
    rounds += 1

    player_card1 = random.randint(1, 10)
    player_card2 = random.randint(1, 10)
    player_card3 = random.randint(1, 10)
    value = player_card1 + player_card2
    dealer_card1 = random.randint(1, 10)
    dealer_card2 = random.randint(1, 10)
    dealer_card3 = random.randint(1, 10)
    value2 = dealer_card1 + dealer_card2
    value3 = 0
    print(value)
    print(value2)

    if value <= 21:
        value4 = player_card1 + player_card2 + player_card3
        print(value4)
    if value2 <= 17:
        value3 = dealer_card2 + dealer_card3 + dealer_card1
        print(value3)
    if value3 <= 21:
        money += 5
        print("You win.")
    else:

    if value4 >= 21:
        print("You win.")
        money += 5
    if value3 >= 21:
        print("You lose.")
    if value4 == value3:
        print("Push.")
        money += 1
    if value4 <= value3:
        print("You lose.")

    print("You have %s dollars." % money)
    print("Round %s." % rounds)

    if money == 0:
        print("You're broke get out.")
        exit(0)
