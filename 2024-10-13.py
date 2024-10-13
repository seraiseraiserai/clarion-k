# list = [1, 5, 6, 11, 2, 15]

# print("length of list:", len(list)) # 6

# print("1st element in list:", list[0]) # 1

# print("2nd element in list:", list[1]) # 5
# print("3rd element in list:", list[2]) # 6
# # # out of bounds
# print("7th element in list:", list[6])

# using a loop
# i = 0
# while (i < len(list)):
#   print(list[i])
#   i = i + 1

# # for loops
# for i in list:
#   print(i)



# create sum function
# def sum(list):
#   s = 0
#   for i in list:
#     s = s + i
#   return(s)
    
    

# print(sum([4, 3, 6])) # 13
# print(sum([1, 2, 3, 4, 5])) # 15






# list = []

# list.append(5)
# list.append(3)
# list.append(11)
# print(list)
# print(len(list))

# # create cumulativeSum function
# def cumulativeSum(list):
#   newlist = []
#   s = 0
#   for i in list:
#     s = s + i
#     newlist.append(s)
#   return(newlist)
  


# # # ex: the cumulative sum of [4, 3, 6] is [4, 7, 13]
# print(cumulativeSum([4, 3, 6]))
# print(cumulativeSum([1, 2, 3, 4, 5]))



# # returns a list of all the even numbers in the input
# def findEvenNumbers(list):
#   newlist = []
#   for i in list:
#     if (i % 2 == 0):
#       newlist.append(i)
#   return(newlist)


# print(findEvenNumbers([1, 2, 3, 4, 5])) # [2, 4]
# print(findEvenNumbers([33, 75, 6, 11, 22])) # [6, 22]
# print(findEvenNumbers([1, 3, 5, 7, 9])) # []
# print(findEvenNumbers([2, 4, 6, 8, 10])) # [2, 4, 6, 8, 10]


# returns a list of all the numbers in the list less than n
# def findSmallerThan(list, n):
  # newlist = []
  # for i in list:
  #   if (i < n):
  #     newlist.append(i)
  # return(newlist)

# print(findSmallerThan([1, 2, 3, 4, 5], 3)) # [1, 2]
# print(findSmallerThan([10, 20, 30, 40, 50], 11)) # [10]
# print(findSmallerThan([20, 40, 3, 11, 15], 0)) # []
# print(findSmallerThan([89, 12, 1, 0, 45], 100)) # [89, 12, 1, 0, 45]


# returns a list of all the numbers in the list that is divisible by n
# def findDivisibleBy(list, n):
#   newlist = []
#   for i in list:
#     if (i % n == 0):
#       newlist.append(i)
#   return(newlist)

# print(findDivisibleBy([2, 3, 5, 4, 7, 20], 2)) # [2, 4, 20]
# print(findDivisibleBy([11, 20, 30, 44, 50], 10))# [20, 30, 50]



# # returns the biggest number in the list
# def findBiggest(list):
#   b = 0
#   for i in list:
#     if (b < i):
#       b = i
#   return(b)


# print(findBiggest([5, 4, 3, 2, 1])) # 5
# print(findBiggest([1, 2, 3, 4, 5, 1])) # 5
# print(findBiggest([6, 23, 544, 89, 1])) # 544






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

    # if (g + 20 > 255):
    #   g = 255
    # else:
    #   g = g + 20

    outputImage[y][x] = [r, g, b]
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