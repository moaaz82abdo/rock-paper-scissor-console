import random
import sys
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal python_wins
        nonlocal player_wins
        class RPM(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3


        playerchoice = input("Enter... \n1 for Rock, \n2 for Paper,  \n3 for Scissors:\n\n")


        if playerchoice not in ["1","2","3"]:
            print("you must choose 1, 2 or 3")
            return play_rps()
        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"you chose {playerchoice}")
        print(f"python chose {computerchoice}")
        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return '✌️✌️ You won!'
            elif player == 2 and computer == 1:
                player_wins += 1
                return '✌️✌️ You won!'
            elif player == 3 and computer == 2:
                player_wins += 1
                return '✌️✌️ You won!'
            elif player == computer:
                return "Draw"
            else:
                python_wins += 1
                return " 🐍🐍 Python won!"
        game_result = decide_winner(player,computer)

        print(game_result)
        nonlocal game_count
        game_count += 1

        print(f"\nGame count:  {str(game_count)}")
        print(f"\nPlayer wins :  { str(player_wins)}")
        print(f"\nPython wins:  {str(python_wins)}")

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
            sys.exit(" 🙋‍♂️ bye")
    return play_rps

play = rps()
play()