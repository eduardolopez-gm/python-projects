from enum import Enum

class Player(Enum):
    P1 = 1
    P2 = 2

def tenis_game(points: list):

    game = ["Love", "15", "30", "40"]
    p1_points = 0
    p2_points = 0
    finished = False
    error = False

    for player in points:

        error = finished

        p1_points += 1 if player == Player.P1 else 0
        p2_points += 1 if player == Player.P2 else 0

        if p1_points >= 3 and p2_points >= 3:
            if not finished and abs(p1_points - p2_points) <= 1:
                print("Deuce" if p1_points == p2_points else
                      "Advantage P1" if p1_points > p2_points else "Advantage P2")
            else:
                finished = True
        else:
            if p1_points < 4 and p2_points < 4:
                print(f"{game[p1_points]} - {game[p2_points]}")
            else:
                finished = True

    print("Points played are incorrect" if error or not finished else
          "Player 1 WIN" if p1_points > p2_points else "Player 2 WIN")


tenis_game([Player.P1, Player.P1, Player.P2, Player.P2,
           Player.P1, Player.P2, Player.P1, Player.P1])

tenis_game([Player.P1, Player.P1, Player.P2, Player.P2,
           Player.P1, Player.P2, Player.P1, Player.P1, Player.P2, Player.P1])

tenis_game([Player.P1, Player.P1, Player.P1, Player.P1, Player.P1, Player.P1])

tenis_game([Player.P1, Player.P1])