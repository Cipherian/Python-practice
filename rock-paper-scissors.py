import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Please input rock, paper or scissors:> ").lower()

    if player == computer:
        print("Computer", computer)
        print("player", player)
        print("Tie")
        break
    elif player == 'rock':
        if computer == 'paper':
            print("Computer", computer)
            print("player", player)
            print("You lose")
            break
        if computer == 'scissors':
            print("Computer", computer)
            print("player", player)
            print("You win")
            break
    elif player == 'scissors':
        if computer == 'paper':
            print("Computer", computer)
            print("player", player)
            print("You win")
            break
        if computer == 'rock':
            print("Computer", computer)
            print("player", player)
            print("You lose")
            break
    elif player == 'paper':
        if computer == 'paper':
            print("Computer", computer)
            print("player", player)
            print("You lose")
            break
        if computer == 'rock':
            print("Computer", computer)
            print("player", player)
            print("You win")
            break
