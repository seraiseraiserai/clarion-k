def isWhite(x, y):  
  return (x + y) % 2 == 0
  

# draw an X inside of a box

# draw a checkerboard
  
# draw a small box
  
# draw 3 diagonal lines

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
