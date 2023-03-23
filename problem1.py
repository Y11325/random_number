#! python3

# SD Computing Studies Assignment
'''
##### Problem 1
Advanced Dungeons and Dragons
optional rolling systems include:
a) roll 4 dice, discard the lowest
b) roll 3 dice, reroll 1's.
Add these as options to your D&D Character Statistics Generator
'''
import random
print("\n\n<<< Dungeons and Dragons Character Generator >>>\n")

def playerRolls():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    d = random.randint(1,6)
    return[a,b,c,d]
    

def normalRoll():
    stats = ["strength", "intelligence", "wisdom", "dexterity", "constitution", "charisma"]

    while True:
        print("\n---character statistics---")
        for i in stats:
            roll = playerRolls()
            print(f"{i}: {roll[0] + roll[1] + roll[2]}")
        
        print("\n")
        again = input("Play again (enter y/n): ")
        if again == "y":
            continue
        elif again == "n":
            print("\n\n")
            main()
            break


def advRoll1():
    stats = ["strength", "intelligence", "wisdom", "dexterity", "constitution", "charisma"]

    while True:
        print("\n---character statistics---")
        for i in stats:
            roll = playerRolls()
            small = min(roll)
            print(f"{i}: {roll[0] + roll[1] + roll[2] + roll[3] - small}")
        
        print("\n")
        again = input("Play again (enter y/n): ")
        if again == "y":
            continue
        elif again == "n":
            print("\n\n")
            main()
            break


def advRoll2():
    stats = ["strength", "intelligence", "wisdom", "dexterity", "constitution", "charisma"]

    while True:
        print("\n---character statistics---")
        for i in stats:
            roll = playerRolls()
            while True:
                if 1 in roll:
                    roll = playerRolls()
                elif 1 not in roll:
                    break
            print(f"{i}: {roll[0] + roll[1] + roll[2]}")

        print("\n")
        again = input("Play again (enter y/n): ")
        if again == "y":
            continue
        elif again == "n":
            print("\n\n")
            main()
            break

    
def main():
    if __name__ == "__main__":
        option = ""
        while option not in ['1','2','3','4']:
            print("===Game Menu===")
            print("1. normal D&D character generator")
            print("2. Advanced D&D: roll 4 dice, discard the lowest")
            print("3. Advanced D&D: roll 3 dice, reroll 1's")
            print("4. Exit\n")
            option = input("Choose an option: ")
        if option == "1":
            normalRoll()
        elif option == "2":
            advRoll1()
        elif option == "3":
            advRoll2()
        elif option == "4":
            print("\n\n===Thanks for playing===\n\n")

main()