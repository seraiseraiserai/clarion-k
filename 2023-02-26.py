# Serai goes shopping, she wants to buy things that are balloons or things that are red
# True or false, will Serai buy the following:
# a blue balloon
# a red pen
# a red balloon
# a blue pen

# Kelly goes shopping. She wants to buy things that are balloons and are red
# True or false, will Kelly buy the following:
# a blue balloon
# a red pen
# a red balloon
# a blue pen

# Shuhua goes shopping. She wants to buy things that are balloons or things that are not red
# True or false, will Shuhua buy the following:
# a blue balloon
# a red pen
# a red balloon
# a blue pen

# Ms.Clara goes shopping. She wants to buy things that are balloons and are not red
# True or false, will Ms.Clara buy the following:
# a blue balloon
# a red pen
# a red balloon
# a blue pen

# # what do I do?
# x = 0
# line = ""
# while(x < 8):
#   line = line + "██"
#   x = x + 1
# print(line)

# # what do I do?
# y = 0
# while(y < 8):
#   x = 0
#   line = ""
#   while(x < 8):
#     line = line + "██"
#     x = x + 1
#   print(line)
#   y = y + 1


def isWhite(x, y):  
  return x == y or x + y == 7

  
# draw stripes

# draw a box

# draw diagonal line


  
# draw a checkerboard

# draw 3 diagonal lines

# draw an X

size = 8
y = 0
while(y < size):
  x = 0
  line = ""
  while(x < size):
    if (isWhite(x, y)):
      line = line + "██"
    else:
      line = line + "  "
    x = x + 1
  print(line)
  y = y + 1
