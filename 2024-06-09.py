# write an interest calculator
def interest(money, rate, years):
  a = 0
  while( a <= years):
    print("year", a, "money ", money)
    money = money * (1 + rate / 100)
    a = a + 1

interest(100, 5, 45)

# exponential graph

# what is an asset
# cars? food?
# bonds, stocks (fund), house, gold, bitcoin
# opportunity cost

# what does it mean to be rich?
# money makes money
# how much money is rich - how much money do I make if I'm already rich?

# taxes
# what are taxes for?
# marginal tax rate
# types of taxes - income, sales, property, capital gains
# ways to pay less taxes

# shopping by scale



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