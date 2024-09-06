# # print small for all numbers < 10, and print BIG for all numbers >= 10
# def printSmallBig(n):
#   a = 0
#   while (a < n):
#     a = a+1
#     if (a < 10):
#       print ("small")
#     else:
#       print ("big")
    

# printSmallBig(13)

# # create multiplication, without using *
# def multiply(m, n):
#   a = 0
#   b = 0
#   while (a < n):
#     a = a + 1
#     b = b + m
#   print (b)

# multiply(5, 3) # 15
# multiply(2, 4) # 8
# multiply(10, 1) # 10
# multiply(5, 0) # 0



# # create division, without using /
# def divide(m, n):
#   a = 0
#   b = m
#   while (b >= n):
#     b = b - n
#     a = a + 1
#   return a

# print(divide(5, 3)) # 1
# print(divide(15, 3)) # 5
# print(divide(16, 4)) # 4


# # create remainder, without using %
# def remainder(m, n):
#   a = 0
#   b = m
#   while (b >= n):
#     b = b - n
#     a = a + 1
#   return b


# print(remainder(5, 3)) # 2
# print(remainder(15, 3)) # 
# print(remainder(16, 4))


# # # Create multiplicationTable
# # multiplicationTable(2, 3)
# # 1*1 = 1
# # 1*2 = 2
# # 1*3 = 3
# # 2*1 = 1
# # 2*2 = 4
# # 2*3 = 6
# def multiplicationTable(m, n):
#   a = 1
#   while (a <= m):
    
    
#     b = 1
#     while (b <= n):
#       print (a, "*", b, "=", a*b)
#       b = b + 1
#     a = a + 1
  

# # multiplicationTable(2, 3)
# # multiplicationTable(3, 5)
# multiplicationTable(8, 8)

# draw a nxn box with #
def drawBox(n):
  x = 1
  y = 1
  while (y <= n):
    x = 1
    b = ""
    while (x <= n):
      x = x + 1
      b = b + "#"
    y = y + 1
    print (b)

drawBox(8)



# # draw a diagonal line with #, with length n
# def drawDiagonalLine(n):
#   print(n)

# drawDiagonalLine(5)



# # draw a diagonal line with #, with length n, going the other way
# def drawDiagonalLine(n):
#   print(n)

# drawDiagonalLine(5)


# How many times would you have to fold a piece of paper in half for it to reach the Moon?
# distance between earth and moon is 384,000km
# a paper is 0.01cm thick


# # create isDivisible
# def isDivisible(m, n):
#   return true

# print(isDivisible(24, 2))
# print(isDivisible(35, 4))
# print(isDivisible(33, 33))
# print(isDivisible(43, 5))
# print(isDivisible(72, 8))

# # create not equal
# def notEqual(m, n):
#   return true


# print(notEqual(3, 3))
# print(notEqual(45, 87))
# print(notEqual("hello", "hello"))



# # create abs(a), which returns the absolute value of a
# def abs(a):
#   return 1

# print(abs(5))
# print(abs(-3))
# print(abs(0))
# print(abs(72))
# print(abs(-9))


# # create max(a, b), which returns the max of the 2 numbers
# def max(a, b):
#   return 1

# print(max(3, 10))
# print(max(10, 3))
# print(max(5, 5))
# print(max(-5, 7))



# # create isPrime(n), which returns true if n is prime, false otherwise
# def isPrime(n):
#   return True

# print(isPrime(3))
# print(isPrime(6))
# print(isPrime(15))
# print(isPrime(17))
# print(isPrime(14))



# # create printPrimes(n), print all the prime numbers < n
# def printPrimes(n):
#   print(1)

# printPrimes(7)
# printPrimes(20)
# printPrimes(100)



# # create sumPrimes(n), sumall the prime numbers < n
# def sumPrimes(n):
#   print(1)

# sumPrimes(7)
# sumPrimes(20)
# sumPrimes(100)