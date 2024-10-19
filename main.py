import matplotlib.image as img
import numpy
import matplotlib.pyplot as pyplot

koalaImage = img.imread("koala.jpg")
kangarooImage = img.imread("kangaroo.jpg")
height, width, _ = koalaImage.shape
outputImage = numpy.zeros([height, width, 3], dtype=numpy.uint8)

y = 0
while (y < height):
  x = 0
  while (x < width):
    r = int(koalaImage[y][x][0])
    g = int(koalaImage[y][x][1])
    b = int(koalaImage[y][x][2])

    ####### code here #######
  
    

    #########################
    outputImage[y][x] = [max(0, min(r, 255)), max(0, min(g, 255)), max(0, min(b, 255))]

    x += 1
  y += 1

pyplot.imsave("outputImage.jpg", outputImage)
print("done")



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