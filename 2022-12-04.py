what do I do?
x = 0
line = ""
while(x < 8):
  line = line + "██"
  x = x + 1
print(line)


what do I do?
y = 0
while(y < 8):
  x = 0
  line = ""
  while(x < 8):
    line = line + "██"
    x = x + 1
  print(line)
  y = y + 1



def isWhite(x, y):
  return True
  

# draw stripes

# draw diagonal line
  
# draw a checkerboard

# draw an X

y = 0
while(y < 8):
  x = 0
  line = ""
  while(x < 8):
    if (isWhite(x, y)):
      line = line + "██"
    else:
      line = line + "  "
    x = x + 1
  print(line)
  y = y + 1
