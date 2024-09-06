
# let's build nim!

# attempted move is the number attempted to remove
# stones is the number of stones left in the pile
# returns true or false
def isValidMove(attemptedMove, stones):
  return attemptedMove <= 5 and attemptedMove > 0 and attemptedMove <= stones

# print(isValidMove(7, 20)) # False
# print(isValidMove(-1, 20)) # False
# print(isValidMove(3, 20)) # True
# print(isValidMove(3, 3)) # True
# print(isValidMove(3, 2)) # False

# player is 1 or 2
# stones is the number of stones left in the pile
# returns a valid move
def getValidMove(player, stones):
  attemptedMove = int(input("player " + str(player) + "'s move: "))
  while (not isValidMove(attemptedMove, stones)):
    print ("invalid, please try again")
    attemptedMove = int(input("player " + str(player) + "'s move: "))
  return attemptedMove

# print(getValidMove(1, 20))

# player is 1 or 2
# stones is the number of stones left in the pile
# returns the number of stones after the player made a move
def makeMove(player, stones):
  print (stones, "stones left")
  a = getValidMove(player, stones)
  return stones - a

# print(makeMove(2, 3))

# finally, build nim
stones = 20
while (stones > 0):
  stones = makeMove(1, stones)
  if (stones == 0):
    print ("player 1 wins!")
  else:
    stones = makeMove(2, stones)
    if (stones == 0):
      print("player 2 wins!")
