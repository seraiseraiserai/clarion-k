# create max(a, b), which returns the max of the 2 numbers
# def max(a, b):
#   if (a < b):
#     return b
#   else:
#     return a

# print(max(3, 10))
# print(max(10, 3))
# print(max(5, 5))
# print(max(-5, 7))



# create isPrime(n), which returns true if n is prime, false otherwise
def isPrime(n):
  a = 2
  while (a < n ):
    if (n % a == 0):
      return False
    a = a + 1
  return True
  
print(isPrime(3))
print(isPrime(6))
print(isPrime(25))
print(isPrime(17))
print(isPrime(14))



# # create printPrimes(n), print all the prime numbers < n
# def printPrimes(n):
#   print(1)

# printPrimes(7)
# printPrimes(20)
# printPrimes(100)



# # create sumPrimes(n), sum all the prime numbers < n
# def sumPrimes(n):
#   print(1)

# sumPrimes(7)
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
