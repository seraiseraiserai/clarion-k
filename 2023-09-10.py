# draw a nxn box with #
# def drawBox(n):
#   y = 0
#   while (y < n):
#     x = 0
#     b = ""
#     while (x < n):
#       b = b + "#"
#       x=x+1
#     y = y + 1
#     print (b)
      

# drawBox(8)


# # draw horizontal stripes
# def drawHorizontalStripes(n):
#   y = 0
#   while (y < n):
#     x = 0
#     b = ""
#     while (x < n):
#       x=x+1
#       if (y % 2==0):
#         b = b +"#"
#       else:
#         b= b + " "
#     y = y + 1
#     print (b)
      

# drawHorizontalStripes(10)




# draw vertical stripes
# def drawVerticalStripes(n):
#   y = 0
#   while (y < n):
#     x = 0
#     b = ""
#     while (x < n):
#       x=x+1
#       if (x % 2==0):
#         b = b +"#"
#       else:
#         b= b + " "
#     y = y + 1
#     print (b)

# drawVerticalStripes(10)




# # draw a hollowed out box
# def drawHollowBox(n):
#   y = 0
#   while (y < n):
#     x = 0
#     b = ""
#     while (x < n):
#       if (y == 0 or y == n - 1 or x == 0 or x == n - 1):
#         b = b +"#"
#       else:
#         b= b + " "
#       x=x+1
#     y = y + 1
#     print (b)

# drawHollowBox(8)



# draw diagonal line
# def drawDiagonalLine(n):
#   y = 0
#   while (y < n):
#     x = 0
#     b = ""
#     while (x < n):
#       if (y == x):
#         b = b +"#"
#       else:
#         b= b + " "
#       x=x+1
#     y = y + 1
#     print (b)


# drawDiagonalLine(10)


# draw diagonal line going the other way
# def drawDiagonalLine(n):
#   y = 0
#   while (y < n):
#     x = 0
#     b = ""
#     while (x < n):
#       if (y + x == n - 1 ):
#         b = b +"#"
#       else:
#         b= b + " "
#       x=x+1
#     y = y + 1
#     print (b)
 
# drawDiagonalLine(5)



# draw a checkerboard
def drawCheckerboard(n):
  y = 0
  while (y < n):
    x = 0
    b = ""
    while (x < n):
      if (y % 2 == 0 and x % 2 == 0 or y % 2 == 1 and x % 2 ==1):
        b = b +"#"
      else:
        b= b + " "
      x=x+1
    y = y + 1
    print (b)

drawCheckerboard(8)



# # draw an X
# def drawX(n):
#   print(n)

# drawX(5)



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