#! python3

# SD Computing Studies Assignment
'''
##### Problem 2
Create a list that contains a deck of cards.
Shuffle and deal 5 card hands to 2 different players.  You may want to make use of the list commands we have previously explored to remove cards when they have been dealt to players.
'''
import random
print("\n\n<=<=Cards dealing game=>=>")

def game():
    myList = ["ace spade", "ace heart", "ace club", "ace diamond", "2 spade", "2 heart", "2 club", "2 diamond", "3 spade", "3 heart", "3 club", "3 diamond", "4 spade", "4 heart", "4 club", "4 diamond", "5 spade", "5 heart", "5 club", "5 diamond","6 spade", "6 heart", "6 club", "6 diamond", "7 spade", "7 heart", "7 club", "7 diamond", "8 spade", "8 heart", "8 club", "8 diamond", "9 spade", "9 heart", "9 club", "9 diamond", "jack spade", "jack heart", "jack club", "jack diamond", "queen spade", "queen heart", "queen club", "queen diamond", "king spade", "king heart", "king club", "king diamond",]
    
    carddeal1 = 0
    carddeal2 = 0
    
    while True:
        if carddeal1 < 5:
            carddeal1 += 1
            player1 = random.choice(myList)
            print(f"PLAYER 1:   {player1}")
            myList.remove(player1)   
        elif carddeal1 == 5:
            print("\n")
            break
            
    while True:
        if carddeal2 < 5:
            carddeal2 += 1
            player2 = random.choice(myList)
            print(f"PLAYER 2:   {player2}")
            myList.remove(player2)   
        elif carddeal2 == 5:
            break


def again():
    while True:
        print("\n")
        keepdealing = input("Play again? (enter y/n): ")
        print("\n")
        if keepdealing == "y":
            game()
        elif keepdealing == "n":
            print("\n\n")
            main()
            break


def main():        
    if __name__ == "__main__":
        inval = ""
        while inval not in ['1','2']:
            print("\nMenu")
            print("1. Play")
            print("2. Exit\n")
            inval = input("Choose an option: ")
        if inval == "1":
            game()
            again()
        elif inval == "2":
            print(29*"*")
            print("\n\n<<---Thanks for playing--->>\n\n")
            


main()