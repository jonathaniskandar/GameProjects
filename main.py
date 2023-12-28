# import game from other script
from Games.RPS import RPS_game


# switch to pick game
def switch(game):
    if game == 1:
        RPS_game()


# list of game can be picked
Game_lists = {
    1: "Rock Paper Scissors",
    2: "",
    3: ""
}

Game_pick = None
while Game_pick != 0:
    Game_pick = int(input("""
Pick game you want to play:
0. To stop
1. Rock Paper Scissors
Your pick:"""))

    switch(Game_pick)

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
