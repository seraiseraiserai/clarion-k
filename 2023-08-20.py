# # what do I do?
# def mystery(n):
#   i = 0
#   while (i <= n):
#     if (i % 2 == 0):
#       print(i)
#     i = i + 1

# mystery(10)


# # what do I do?
# def mystery(m, n):
#   i = 0
#   s = 0
#   while (i < n):
#     i = i + 1
#     s = s + m
#   print (s)

# mystery(2, 3) # 6
# mystery(4, 4) # 16
# mystery(12, 0) # 0



# # create division, without using /
# def divide(a, b):
#   p = 0
#   while (a >= b):
#     p = p + 1
#     a = a - b
#   return p

# print(divide(7, 3)) # 2
# print(divide(15, 3))# 5
# print(divide(16, 4))# 4



# # create remainder, without using %
# def remainder(a, b):
#   p = 0
#   while (a >= b):
#     p = p + 1
#     a = a - b
#   return a
  

# print(remainder(7, 3)) # 1
# print(remainder(17, 3)) # 2
# print(remainder(16, 4)) # 0



# print:
#   left
#   right!
# n times
# def printLeftRight(n):
#   a = 0
#   while (a < n):
#     a = a + 1
#     if a % 2 == 0:
#       print("right")
#     else: 
#       print("left")

# printLeftRight(5)



# print:
#   duck
#   duck
#   goose
# n times
# def printDuckDuckGoose(n):
#   a = 0
#   while (a < n):
#     a = a + 1
#     if a % 3 == 0:
#       print("goose")
#     else: 
#       print("duck")


# printDuckDuckGoose(9)


# a = "blah"
# a = a + "p"
# print(a)


# # # print o... with a length based on n
# def ooo(n):
#   a = 0
#   b = ""
#   while (a < n):
#     a = a + 1
#     b = b + "o"
#   print(b)

# ooo(3) # ooo
# ooo(6) # oooooo
# ooo(13) # ooooooooooooo



# print lololol... with a length based on n
def lol(n):
  a = 0
  b = ""
  while (a < n):
    a = a + 1
    if a % 2 == 0:
      b = b + "o"
    else:
      b = b + "l"
  print(b)


lol(15) # lolol


# # print small for all numbers < 10, and print BIG for all numbers >= 10
# def printSmallBig(n):
#   print("small")

# printSmallBig(3)
# printSmallBig(13)


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