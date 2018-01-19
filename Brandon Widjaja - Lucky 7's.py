import random


print("Welcome to Lucky 7's. You have 15 dollars.")

left_over_money = 0

rounds = 1

money = 15

most_money = money

print("Round %s" % rounds)
stop_at_round = 0
while money > 0:

    money -= 1
    rounds += 1
    print("You have %s dollars." % money)

    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)

    print(num1 + num2)

    if (num1 + num2) == 7:
        money += 5
        print("You win.")
        print("Round %s" % rounds)
        if money >= most_money:
            most_money = money
            stop_at_round = rounds
    else:
        print("You lost.")
        print("Round %s" % rounds)

print("You played %s rounds." % rounds)
print("You should have stopped at round %s." % stop_at_round)
print("When you had this much money %s." % most_money)
print("Game Over.")
