player1 = input("what is player 1's move? ")
player2 = input("what is player 2's move? ")
if (player1 == "rock" and player2 == "paper"):
    print("player2 has won!")
elif (player1 == "scissors" and player2 == "rock"):
    print("player2 has won!")
elif (player1 == "paper" and player2 == "scissors"):
    print("player2 has won!")
elif (player1 == "paper" and player2 == "rock"):
    print("player1 has won!")
elif (player1 == "rock" and player2 == "scissors"):
    print("player1 has won!")
elif (player1 == "scissors" and player2 == "paper"):
    print("player1 has won!")
else:
    print("it is a tie!")

# if (player1 == "rock" and player2 == "scissors"):
