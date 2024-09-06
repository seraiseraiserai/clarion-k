# # What do I do?
# def mystery(list):
#   a = 0
#   for i in list:
#     a = a + i
#   return a / len(list)

# print(mystery([5, 4, 1, 2, 3])) # 3
# print(mystery([5, 5, 5, 5])) # 5


# # returns a list of all the even numbers in the input
# def findEvenNumbers(list):
#   newlist = []
#   for i in list:
#     if i % 2 == 0:
#       newlist.append(i)
#   return newlist


# print(findEvenNumbers([1, 2, 3, 4, 5])) # [2, 4]
# print(findEvenNumbers([33, 75, 6, 11, 22])) # [6, 22]
# print(findEvenNumbers([1, 3, 5, 7, 9])) # []
# print(findEvenNumbers([2, 4, 6, 8, 10])) # [2, 4, 6, 8, 10]




# # returns the biggest number in the list
# def findBiggest(list):
#   a = 0
#   for i in list:
#     if a < i:
#       a = i
#   return a

# print(findBiggest([1, 3, 2, 4, 5])) # 5
# print(findBiggest([6, 23, 544, 89, 1])) # 544




# # write allLessThan, returns True if all the numbers in the list are less than n
# def allLessThan(list, n):
#   for i in list:
#     if i > n:
#       return False

#   return True

# print(allLessThan([1, 2, 3, 4, 5], 10)) # T
# print(allLessThan([1, 2, 3, 4, 5], 3)) # F
# print(allLessThan([10, 20, 30, 40, 50], 3)) # F
# print(allLessThan([5, 4, 3, 2, 1], 3)) # F
# print(allLessThan([34, 2, 5, 76, 11], 100)) # T


# write an interest calculator
def interest(money, rate, years):
  y = 0
  while(y <= years):
    y = y + 1 
    money= money + money*rate / 100
  return money


print(interest(100, 5, 10))
print(interest(10000, 7, 30))


print(3/4)


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