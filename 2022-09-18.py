# What do I do?
# a = 0.01
# b = 0
# while (a <= 38400000000):
#   a = a * 2
#   b = b + 1
# print(b)

# What do I do?
# a = 1
# while (a > 0):
#     a = a + 1
# print(a)

# What do I do?
# a = 15
# print("hello" + str(a))

# let's write a stopwatch!
import time
milliseconds = 0

while (milliseconds <= 99):
  if (milliseconds <= 9):
    print( "0" + str(milliseconds), end="\r")
  else:
    print (milliseconds, end="\r")
  milliseconds = milliseconds + 1
  time.sleep (0.01)


# print(1, end="\r")
# time.sleep(0.5)
# print(2, end="\r")
# time.sleep(0.5)
# print(3, end="\r")
# time.sleep(0.5)
# print(4, end="\r")
# time.sleep(0.5)
# print(5, end="\r")
# time.sleep(0.5)
