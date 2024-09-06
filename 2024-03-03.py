# # what do I do?
# def mystery(list):
#   newList = []
#   for i in list:
#     if (i % 3 == 0):
#       newList.append(i)
#   return newList

# print(mystery([1, 2, 3, 4, 5, 6]))
# print(mystery([9, 9, 9, 9, 9]))
# print(mystery([2, 4, 6, 8, 10]))


# # # write allLessThan, returns True if all the numbers in the list are less than n
# def allLessThan(list, n):
#   newList = []
#   for i in list:
#     if (i < n):
#       newList.append(i)
#   return newList

# print(allLessThan([1, 2, 3, 4, 5], 10)) # [1, 2, 3, 4, 5]
# print(allLessThan([1, 2, 3, 4, 5], 3)) # [1, 2]
# print(allLessThan([10, 20, 30, 40, 50], 3)) # []
# print(allLessThan([5, 4, 3, 2, 1], 3)) # [2, 1]
# print(allLessThan([34, 2, 5, 76, 11], 100)) # [34, 2, 5, 76, 11]

# # write allLessThan, returns True if all the numbers in the list are less than n
# def allLessThan(list, n):
#   for i in list:
#     if (i >= n):
#       return False
#   return True


# print(allLessThan([1, 2, 3, 4, 5], 10)) # true
# print(allLessThan([1, 2, 3, 4, 5], 3)) # false
# print(allLessThan([10, 20, 30, 40, 50], 3)) # false
# print(allLessThan([5, 4, 3, 2, 1], 3)) # false
# print(allLessThan([34, 2, 5, 76, 11], 100)) # true



# # write atLeastOneLessThan, returns True if at least one number in the list is less than n
# def atLeastOneLessThan(list, n):
#     for i in list:
#       if (i < n):
#         return True
#     return False

# print(atLeastOneLessThan([1, 2, 3, 4, 5], 3)) # True
# print(atLeastOneLessThan([1, 2, 3, 4, 5], 0)) # False
# print(atLeastOneLessThan([10, 20, 30, 40, 50], 3)) # False
# print(atLeastOneLessThan([5, 4, 3, 2, 1], 3)) # True
# print(atLeastOneLessThan([34, 2, 5, 76, 11], 1)) # False




# # create a list of ["ah", "ahh", "ahhh", "ahhhh", ...] based on an input of how many h's
# def ahhh():
#   hCount = int(input("How many h? "))
#   h = 0
#   a = "a"
#   newList=[]
#   while (h <= hCount):
#     h = h + 1
#     a = a + "h"
#     newList.append(a)
#   print (newList)


# ahhh()



# # returns a list of all the numbers that's in both numbersA and numbersB
# def intersection(numbersA, numbersB):
#   newList = []
#   for a in numbersA:
#     for b in numbersB:
#       if (a==b):
#         newList.append(a)
#   return newList



# print(intersection([1, 2, 3, 4, 5], [3, 4, 5, 6])) # [3, 4, 5]
# print(intersection([4, 12, 8, 12, 3], [3, 12])) # [3, 12]
# print(intersection([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])) # [1, 2, 3, 4, 5]
# print(intersection([1, 2, 3, 4, 5], [6, 7, 8, 9])) # []


# returns a list of all the numbers that aren't in filteredNumbers
def filterNumbers(numbers, filteredNumbers):
  newList = []
  for n in numbers:
    foundN = False
    for f in filteredNumbers:
      if (n == f):
        foundN = True
    if (foundN == False):  
      newList.append(n)
  return newList

print(filterNumbers([1, 2, 3, 4, 5], [2, 4])) # [1, 3, 5]
print(filterNumbers([4, 12, 8, 12, 3], [3, 12])) # [4, 8]
print(filterNumbers([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])) # []
print(filterNumbers([1, 2, 3, 4, 5], [100, 200])) # [1, 2, 3, 4, 5]

