'''
AUTHOR:NIKHIL SAJU
DATE:6/12/24
DESCRIPTION:Write a program to play a sticks game in which there are 16 sticks.
Two players take turns to play the game. Each player picks one set of sticks (needn’t be adjacent) during his turn.
A set contains 1, 2, or 3 sticks. The player who takes the last stick is the loser. The number of sticks in the set is to be input.
'''





def play_stick_game():
    sticks=16
    current_player=1
    while sticks>0:
        print(f"\nCurrent number of sticks: {sticks}")
        move=int(input(f"Player{current_player},how many sticks do you want to remove? (Choose 3,2 or 1)"))
        if move not in [1,2,3]:
            print("Invalid move")
            continue
        if move>sticks:
            print(f"Not enough sticks.You can only remove up to {sticks}")
            continue
        sticks-=move
        if sticks==0:
            print(f"\nPlayer {current_player} removed the last stick")
            print(f"Player{current_player} loses")
        current_player=3-current_player
play_stick_game()