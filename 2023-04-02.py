# list = [4, 5, 9, 12, 23, 2, 7]

# for l in list:
#   if (l % 2 == 0):
#     print (l)

# what do I do?
# list = [5, 4, 3, 2, 1]
# b = 0
# for l in list: 
#    b = b + l  
# print (b)

# appending lists
# list = []
# list.append(1)
# list.append(2)
# list.append(3)
# print(list)

# # create a list of all the even numbers from 0 to 100
# list = []
# i = 0
# while(i < 101):
#    if (i % 2 == 0):
#     list.append(i)
#    i = i + 1
# print(list)


# create cumulativeSum function
def cumulativeSum(list):
  sum = 0
  output = []
  for l in list:
   sum = sum + l
   output.append(sum)
  return output

# ex: the cumulative sum of [4, 3, 6] is [4, 7, 13]
# print(cumulativeSum([4, 3, 6]))
print(cumulativeSum([1, 2, 3, 4, 5])) # [1, 3, 6, 10,15]

# # list can also contain strings
# list = ["hello", "world", "!"]
# print(list)

# # write a report card creator
# # ask for number of classes, name of each class, and grade
# def report_card():
#   classesCount = int(input("How many classes did you take? "))

# report_card()