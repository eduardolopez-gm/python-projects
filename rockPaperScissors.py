def rock_paper_scissors(games):
    
    rules = {"rock": "scissors",
            "paper": "rock",
            "scissors": "paper" }

    # Initialize the game
    player_one = 0
    player_two = 0
    # Iterate over the different games
    for game in games:
        player_one_game = game[0]
        player_two_game = game[1]
        if player_one_game != player_two_game:
            if player_two_game in rules[player_one_game]:
                player_one += 1
            else:
                player_two += 1

    return "Tie GAME" if player_one == player_two else "Player 1 Wins" if player_one > player_two else "Player 2 Wins"

# Method will accept a tuple or an array of tuples
print(rock_paper_scissors([("rock", "paper"), ("scissors", "paper"), ("paper", "scissors")]))
print(rock_paper_scissors([("scissors", "paper")]))
print(rock_paper_scissors([("paper", "scissors")]))
print(rock_paper_scissors([("paper", "paper")]))

