def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 wins!"
    elif beats[p2] == p1:
        return "Player 2 wins"
    else:
        return "Draw!"


print(rps("scissors", "scissors"))