# # # What do I do?
# def mystery(list):
#   a = list[0]
#   for i in list:
#     if (a >= i):
#       a = i
#   return a

# print(mystery([1, 2, 3, 4, 5])) # 1
# print(mystery([5, 4, 3, 2, 1])) # 1
# print(mystery([6, 23, 4, 544, 89])) # 4




# # write countEvens, returns the number of even numbers in the list
# def countEvens(list):
#   a=0
#   for i in list:
#     if(i % 2 == 0):
#       a = a + 1
#   return a


# print(countEvens([1, 2, 3, 4, 5])) # 2
# print(countEvens([5, 4, 3, 2, 1])) # 2
# print(countEvens([6, 23, 544, 88, 1])) # 3



# # write average, returns the average of all the numbers in the list
# def average(list):
#   a = 0
#   # len(list)
#   for i in list:
#     a = a + i
#   return a / len(list)  


# print(average([1, 2, 3, 4, 5])) # 3
# print(average([6, 23, 3, 544, 89])) # 133



# write findBiggest, returns the biggest number in the list
def findBiggest(list):
    a = list[0]
    for i in list:
      if (a < i):
        a = i
    return a


# print(findBiggest([1, 2, 3, 4, 5])) # 
# print(findBiggest([5, 4, 3, 2, 1]))
# print(findBiggest([6, 23, 4, 544, 89]))



# write findSecondBiggest, returns the second biggest number in the list
def findSecondBiggest(list):
  findBiggest(list)
  b = findBiggest(list)
  a = 0
  for i in list:
    if(i != b and i > a):
      a = i
  return a 



print(findSecondBiggest([1, 2, 3, 4, 5])) # 4
print(findSecondBiggest([5, 4, 3, 2, 1])) # 4
print(findSecondBiggest([6, 23, 1, 544, 89])) # 89



# # write an interest calculator
# def interest(money, rate, years):

# print(interest(100, 5, 10))
# print(interest(10000, 7, 30))





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