# what do I do?
# def mystery(n):
#   if (n % 2 == 0):
#     return n + 2
#   else:
#     return n + 1

# print(mystery(3))
# print(1 + mystery(2))
# print(mystery(-5))


# # what do I do?
# def mystery2(a, b):
#   sum = 0
#   while (b > 0):
#     sum = sum + a
#     b = b - 1
#   return sum

# print(mystery2(5, 4))
# print(mystery2(1, 3))
# print(mystery2(1, 3))



# let's build nim!

def isValidMove(attemptedMove, stones):
  return attemptedMove <= stones and attemptedMove <= 5 and attemptedMove > 0
  
def getValidMove(player, stones):
  attemptedMove = int(input(player + "'s move: "))
  while (not isValidMove(attemptedMove, stones)):
    print ("please give me another number")
    attemptedMove = int(input(player + "'s move: "))
  return attemptedMove

def makeMove(player, stones):
  validMove = getValidMove(player, stones)
  stones = stones - validMove
  return stones

stones = 20
while stones > 0:
  stones = makeMove("Player 1", stones)
  print (stones)
  if (stones == 0):
    print ("Player 1 wins")
  if stones > 0:
    stones = makeMove("Player 2", stones)
    print (stones)
    if (stones == 0):
      print ("Player 2 wins")
