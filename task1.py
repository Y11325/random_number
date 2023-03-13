#! python3

# SD Computing Studies Assignment
'''
##### Task 1
Number Guessing Game
Have the computer generate a random number from 1 to 100.  The players will try to guess the number, and the computer will tell them if they are too high or too low.  Play continues until they guess correctly at which point the computer tells them how many guesses it took.
(2 points) 
'''
print("---Guess a number between 1 and 100---")
import random
x = random.randrange(100)
n = int(input("\n\nEnter an integer: "))
attempts = 0

while n != x:
    print(f"\nWRONG! Keep guessing!\n")
    attempts += 1
    if n > x:
        print("The number you entered is too high, try to guess lower!")
        n = int(input("\n\nEnter another integer: "))

    elif n < x:
        print("The number you entered is too low, try to guess higher!")
        n = int(input("\n\nEnter another integer: "))

    if n == x:
        break
print("\n\n")
print(30*"*")
print(f"Correct!!!\nYou used {attempts} attempts!\nCongratulation!!!\n\n")
