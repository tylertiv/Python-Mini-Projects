from random import *

gameLoop = True
choices = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0
player = comp = 0


print("\n======== Score ========= \n"
      "Player: " + str(player_score) + "   Computer: " + str(computer_score) + '\n'
      "========================")
player = input("Choose a weapon: \n"
                "(1) Rock \n"
                "(2) Paper \n"
                "(3) Scissors \n"
                  "(q) Quit \n")
if player != 'q':
    player = int(player) - 1
    comp = randrange(0, 3)
    print("You picked: " + choices[player] + "\nComputer picked: " + choices[comp])

while player != 'q':
    if player != comp:
        if player == 0:
            if comp == 1:
                print("Computer wins!")
                computer_score += 1
            else:
                print("Player wins!")
                player_score += 1
        elif player == 1:
            if comp == 2:
                print("Computer wins!")
                computer_score += 1
            else:
                print("Player wins!")
                player_score += 1
        else:
            if comp == 0:
                print("Computer wins!")
                computer_score += 1
            else:
                print("Player wins!")
                player_score += 1
    else:
        print("Tie, nobody wins.")
    print("\n======== Score ========= \n"
          "Player: " + str(player_score) + "   Computer: " + str(computer_score) + '\n'
                                                                                   "========================")
    player = input("Choose a weapon: \n"
                   "(1) Rock \n"
                   "(2) Paper \n"
                   "(3) Scissors \n"
                   "(q) Quit \n")
    if player != 'q':
        player = int(player) - 1
        comp = randrange(0, 3)
        print("You picked: " + choices[player] + "\nComputer picked: " + choices[comp])
