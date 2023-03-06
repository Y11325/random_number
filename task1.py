#! python3

# SD Computing Studies Assignment
'''
##### Task 1
Number Guessing Game
Have the computer generate a random number from 1 to 100.  The players will try to guess the number, and the computer will tell them if they are too high or too low.  Play continues until they guess correctly at which point the computer tells them how many guesses it took.
(2 points) 
'''
import random
def rand1(max):
    for i in range(5):
        x = random.randrange(max)
        print(x, end=" ")

def rand2():
    for i in range (1):
        x = random.randint(1,100)
        print(x, end=" ")

rand2()