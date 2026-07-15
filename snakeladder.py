import random

snakes = {
    17: 7,
    54: 34,
    62: 19,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}
ladders = {
    4: 14,
    9: 31,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    63: 81,
    71: 91,
}
player1 = 0
player2 = 0
turn = 1

print("===== SNAKE AND LADDER GAME ====")

while True:
    input(f"\nPlayer {turn}, press enter to roll the dice...")
    
    dice = random.randint(1,6)
    print("Dice:", dice)

    if turn == 1:
        if player1 + dice <= 100:
            player1 += dice

        if player1 in ladders:
            print("ladder! climb up")
            player1 = ladders[player1]
        
        elif player1 in snakes:
            print("snake go down. ")
            player1 = snakes[player1]

        print("Player 1 Position:", player1)

        if player1 == 100:
            print("\n player 1 wins!")
            break
        turn = 2

    else:
        if player2 + dice <= 100:
            player2 += dice

        if player2 in ladders:
            print("ladder! climb up. ")
            playe2 = ladders[player2]

        elif player2 in snakes:
            print("Snakes! go down. ")
            player2 = snakes[player2]

        print("Player 2 Position:", player2)

        if player2 == 100:
            print("\n player 2 wins!")
            break

        turn = 1