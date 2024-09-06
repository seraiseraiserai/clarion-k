# create printAllDivisible, which prints all the numbers n is divisible by
# def printAllDivisible(n):
#   a = 0
#   while(a < n):
#     a = a + 1
#     if (n % a == 0):
#       print (a)

# printAllDivisible(6)
# printAllDivisible(7)
# printAllDivisible(24)
# printAllDivisible(25)



# create isPrime(n), which returns true if n is prime, false otherwise
def isPrime(n):
  a = 1
  while(a < n - 1):
    a = a + 1
    if (n % a == 0):
      return False
  return True



# print(isPrime(3))
# print(isPrime(6))
# print(isPrime(25))
# print(isPrime(17))
# print(isPrime(14))



# create printPrimes(n), print all the prime numbers < n
# def printPrimes(n):
#   a = 0
#   while(a < n):
#     a = a + 1
#     if (isPrime(a)):
#      print (a)

# printPrimes(7)
# printPrimes(20)
# printPrimes(100)



# create sumPrimes(n), sum all the prime numbers < n
def sumPrimes(n):
  a = 0
  b = 0
  while(a < n):
    a = a + 1
    b = b + a
    if (isPrime(a)):
      print (a)



sumPrimes(7)
# sumPrimes(20)
# sumPrimes(100)



# let's build nim!

# attempted move is the number attempted to remove
# stones is the number of stones left in the pile
# returns true or false
# def isValidMove(attemptedMove, stones):


# player is 1 or 2
# stones is the number of stones left in the pile
# returns a valid move
# def getValidMove(player, stones):
  # attemptedMove = int(input(player + "'s move: "))
  # print(attemptedMove)

# player is 1 or 2
# stones is the number of stones left in the pile
# returns the number of stones after the player made a move
# def makeMove(player, stones):


# finally, build nim
# stones = 20
