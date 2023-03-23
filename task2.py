#! python3

# SD Computing Studies Assignment
'''
##### Task 2
Coin Toss
Ask the player to choose heads or tails.
Toss a coin to determine what the coin will be, and then tell the player if they were correct.
(2 points)
'''
print("\n\n<<<---Heads or Tails--->>>")
import random

while True:
    coin = random.randint(0,1)
    print("\nCoin tossed...")
    print(100*"*")

    guess = input("\nGuess heads or tails: ")
    if guess == "heads":
        guess = 0
    elif guess == "tails":
        guess = 1

    if guess != coin:
        print("\nWrong!\n\n")
        again = input("Play again (enter yes or no):")
        if again == "yes":
            continue
        elif again == "no":
            break
    elif guess == coin:
        print("\nCorrect!\n\n")
        again = input("Play again (enter yes or no):")
        if again == "yes":
            continue
        elif again == "no":
            break
print("\n---Thanks for playing---\n\n")