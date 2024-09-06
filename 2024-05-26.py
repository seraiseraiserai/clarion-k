# write an interest calculator
def interest(savings, rate, years):
  a = 0
  money = 0
  while( a <= years):
    print("year", a, "money ", money)
    money = money * (1 + rate / 100) + savings
    a = a + 1

interest(808 * 12, 5, 45)

# exponential graph

# making a budget
# find living expenses, figure out cost
# cut down on costs

# item	cost
# rent	2995
# car	219.38
# water	108
# electricity	209
# grocery	360
# clothes	130
# movies	15
# entertainment	127
# travel	166.6666667
# eating out	120
# savings	808

# SUM	5258.046667
# monthly budget	5258.666667

# what does it mean to be rich?
# money makes money
# how much money is rich - how much money do I make if I'm already rich?







# import matplotlib.image as img
# import numpy
# import matplotlib.pyplot as pyplot

# koalaImage = img.imread("koala.jpg")
# kangarooImage = img.imread("kangaroo.jpg")
# height, width, _ = koalaImage.shape
# outputImage = numpy.zeros([height, width, 3], dtype=numpy.uint8)

# y = 0
# while (y < height):
#   x = 0
#   while (x < width):
#     r = int(koalaImage[y][x][0])
#     g = int(koalaImage[y][x][1])
#     b = int(koalaImage[y][x][2])

#     outputImage[y][x] = [r, g, b]
#     x += 1
#   y += 1

# pyplot.imsave("outputImage.jpg", outputImage)



# make the koala redder

# make the koala greener

# make the koala grayscale

# make the koala sepia

# make the koala brighter

# make the koala darker

# inverse the color of the koala

# flip the koala horizontally

# flip the koala vertically

# rotate the koala 90 degrees

# make the koala smaller

# crop the koala

# half of the image is kangaroo, half is koala

# place the kangaroo image over the koala image

# add a colored gradient

# transition the kaola image into the kangaroo image