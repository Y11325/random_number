#! python3

# SD Computing Studies Assignment
'''
##### Task 3
Rock Paper Scissors
Create the classic "Rock, Paper Scissors Game"
(5 points)
Extension:
Play the classic "Rock Paper Scissors Lizard Spock" game
https://www.youtube.com/watch?v=Z2Dwxv-EMTM
'''
import random

def game1():
    while True:
        move = input("\nEnter rock, paper, or scissors (spelling counts): ")
        computer = random.randint(0,2)

        if move == "rock":
            move = 0
        elif move == "paper":
            move = 1
        elif move == "scissors":
            move = 2
        
        if move == computer:
            print("Draw")
        elif move == 0 and computer == 2:
            0 > 2 is True
            print("You win, rock beats scissors")
        elif move == 2 and computer == 0:
            2 < 0 is True
            print("You lose, rock beats scissors")
        elif move < computer:
            print("you lose, ",end="")
            if move == 0 and computer == 1:
                move = "rock"
                computer = "paper"
                print(f"computer: {computer} beats you: {move}")
            elif move == 1 and computer == 2:
                move = "paper"
                computer = "scissors"
                print(f"computer: {computer} beat you: {move}")
        elif move > computer:
            print("you win, ",end="")
            if computer == 0 and move == 1:
                computer = "rock"
                move = "paper"
                print(f"you: {move} beats computer: {computer}")
            elif computer == 1 and move == 2:
                computer = "paper"
                move = "scissors"
                print(f"you: {move} beat computer: {computer}")
        
        print("\n")
        again = input("Play again (enter y/n): ")
        if again == "y":
            continue
        elif again == "n":
            main()
            break

def game2():
    while True:
        move = input("\nEnter rock, paper, scissors, lizard, or spock (spelling counts): ")
        #Just found a simpler way of doing things :D
        stuff = ["rock", "paper", "scissors", "lizard", "spock"]
        computer = random.choice(stuff)

        if move == computer:
            print(f"\nDraw!\ncomputer: {computer}\nyou: {move}")
        elif move == "rock":
            if computer == "scissors":
                print(f"\nYou win!\nRock crushes scissors\ncomputer: {computer}\nyou: {move}")
            elif computer == "lizard":
                print(f"\nYou win!\nRock crushes lizard\ncomputer: {computer}\nyou: {move}")
            if computer == "paper":
                print(f"\nYou lose!\nPaper covers rock\ncomputer: {computer}\nyou: {move}")
            elif computer == "spock":
                print(f"\nYou lose!\nSpock vaporizes rock\ncomputer: {computer}\nyou: {move}")
        elif move == "paper":
            if computer == "rock":
                print(f"\nYou win!\nPaper covers rock\ncomputer: {computer}\nyou: {move}")
            elif computer == "spock":
                print(f"\nYou win!\nPaper disproves spock\ncomputer: {computer}\nyou: {move}")
            if computer == "lizard":
                print(f"\nYou lose!\nLizard eats paper\ncomputer: {computer}\nyou: {move}")
            elif computer == "scissors":
                print(f"\nYou lose!\nScissors cuts paper\ncomputer: {computer}\nyou: {move}")
        elif move == "scissors":
            if computer == "paper":
                print(f"\nYou win!\nScissors cuts paper\ncomputer: {computer}\nyou: {move}")
            elif computer == "lizard":
                print(f"\nYou win!\nScissors decapitates lizard\ncomputer: {computer}\nyou: {move}")
            if computer == "rock":
                print(f"\nYou lose!\nRock crushes scissors\ncomputer: {computer}\nyou: {move}")
            elif computer == "spock":
                print(f"\nYou lose!\nSpock smashes scissors\ncomputer: {computer}\nyou: {move}")
        elif move == "lizard":
            if computer == "paper":
                print(f"\nYou win!\nLizard eats paper\ncomputer: {computer}\nyou: {move}")
            elif computer == "spock":
                print(f"\nYou win!\nLizard poisons spock\ncomputer: {computer}\nyou: {move}")
            if computer == "rock":
                print(f"\nYou lose!\nRock crushes lizard\ncomputer: {computer}\nyou: {move}")
            elif computer == "scissors":
                print(f"\nYou lose!\nScissors decapitates lizard\ncomputer: {computer}\nyou: {move}")
        elif move == "spock":
            if computer == "scissors":
                print(f"\nYou win!\nSpock smashes scissors\ncomputer: {computer}\nyou: {move}")
            elif computer == "rock":
                print(f"\nYou win!\nSpock vaporizes rock\ncomputer: {computer}\nyou: {move}")
            if computer == "lizard":
                print(f"\nYou lose!\nLizard poisons spock\ncomputer: {computer}\nyou: {move}")
            elif computer == "paper":
                print(f"\nYou lose!\nPaper disproves spock\ncomputer: {computer}\nyou: {move}")
                print("\n")
                
        again = input("Play again (enter y/n): ")
        if again == "y":
            continue
        elif again == "n":
            main()
            break


def main():
    if __name__ == "__main__":
        option = ""
        while option not in ['1','2','3']:
            print("\n\n")
            print("<<<===---Game Menu---===>>>")
            print("1. Classic \"Rock, Paper Scissors Game\"")
            print("2. \"Rock Paper Scissors Lizard Spock\" game")
            print("3. Exit\n")
            option = input("Choose an option: ")
        if option == "1":
            game1()
        elif option == "2":
            game2()
        elif option == "3":
            print("\n\n<<<===---Thanks for playing---===>>>\n\n")
main()