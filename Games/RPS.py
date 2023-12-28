# this is rock paper scissors game
from random import randint


def compare(p, c):
    if p == c:
        print("Tie")
    elif p == 1:
        if c == 2:
            print("Computer Wins!")
        else:
            print("Player Wins!")
    elif p == 2:
        if c == 1:
            print("Player Wins!")
        else:
            print("Computer Wins")
    elif p == 3:
        if c == 1:
            print("Computer Wins!")
        else:
            print("Player Wins!")
    print("=====END=====")

choice = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}


def RPS_game():
    computer_choice = randint(1, 3)

    print("\nIt's Rock Paper Scissors Game\nPlease Pick by Entering Number:")
    player_choice = int(input("1: Rock\n2: Paper\n3: Scissors\nYour Pick: "))

    print(f"\nThe Computer picked {choice[computer_choice]}")
    print(f"The Player picked {choice[player_choice]}")

    compare(player_choice, computer_choice)
