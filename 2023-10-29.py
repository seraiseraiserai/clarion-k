# create printAllDivisible, which prints all the numbers n is divisible by
# def printAllDivisible(n):
#   a = 0
#   while (a <= n):
#     a = a + 1
#     if (n % a== 0):
#       print (a)

# printAllDivisible(6)
# printAllDivisible(7)
# printAllDivisible(24)
# printAllDivisible(25)



# create isPrime(n), which returns true if n is prime, false otherwise
def isPrime(n):
  a = 0
  b = 0
  while (a <= n):
    a = a + 1
    if (n % a== 0):
      b = b + 1
  return (b == 1 or b == 2)


# print(isPrime(3))
# print(isPrime(6))
# print(isPrime(25))
# print(isPrime(17))
# print(isPrime(14))



# # create printPrimes(n), print all the prime numbers < n
def printPrimes(n):
  a = 0
  while (a < n):
    a = a + 1  
    if (isPrime(a)):
      print (a)

# printPrimes(100)


# # create sumPrimes(n), sum all the prime numbers < n
def sumPrimes(n):

  a = 0
  b = 0
  while (a < n):
    a = a + 1  
    if (isPrime(a)):
      b = b + a
  print (b)


# sumPrimes(10)
# sumPrimes(20)
# sumPrimes(100)



# let's build nim!

# attempted move is the number attempted to remove
# stones is the number of stones left in the pile
# returns true or false
def isValidMove(attemptedMove, stones):
  return attemptedMove <= 5 and attemptedMove > 0 and attemptedMove <= stones


# player is 1 or 2
# stones is the number of stones left in the pile
# returns a valid move
def getValidMove(player, stones):
  print(str(stones) + " stones left")
  attemptedMove = int(input(player + "'s move: "))
  if (isValidMove(attemptedMove, stones)):
    return attemptedMove
  else:
    print ("Invalid, please try again")
    while (not isValidMove(attemptedMove, stones)):
       attemptedMove = int(input(player + "'s move: "))
    return attemptedMove

print(getValidMove("1", 4))


# player is 1 or 2
# stones is the number of stones left in the pile
# returns the number of stones after the player made a move
# def makeMove(player, stones):


# finally, build nim
# stones = 20
