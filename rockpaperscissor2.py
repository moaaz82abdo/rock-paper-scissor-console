import random
import sys
from enum import Enum

class RPM(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

playagain = True

while playagain:
    playerchoice = input("Enter... \n1 for Rock, \n2 for Paper,  \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("you must enter 1,2, or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("you chose " + playerchoice)
    print("python chose " + computerchoice)

    if player == 1 and computer == 3:
        print("You won!")
    elif player == 2 and computer == 1:
        print("You won!")
    elif player == 3 and computer == 2:
        print("You won!")
    elif player == computer:
        print("Draw")
    else:
        print("Python won!")
    playagain = input("\nplay again? \ny for yes \nq for quit")
    if playagain == "y":
        continue
    else:
        sys.exit()