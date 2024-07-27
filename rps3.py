import random
import sys
from enum import Enum



def play_rps():
    class RPM(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3


    playerchoice = input("Enter... \n1 for Rock, \n2 for Paper,  \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("you must choose 1, 2 or 3")
        return play_rps()
    player = int(playerchoice)

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


    print("\nplay again? ")
    while True:
      playagain = input("\ny for yes \nq for quit")

      if playagain.lower() not in ["y", "q"]:
        continue
      else:
          break
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("thanks for playing")
        sys.exit("bye")
play_rps()