# write an interest calculator
def interest(money, rate, years):
  a = 0
  while( a <= years):
    print("year", a, "money ", money)
    money = money * (1 + rate / 100)
    a = a + 1

interest(1000000, 5, 10)

# taxes
# what are taxes for?
# marginal tax rate https://engaging-data.com/tax-brackets/
# types of taxes - income, sales, property, capital gains
# paying taxes
# ways to pay less taxes
# retirement




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