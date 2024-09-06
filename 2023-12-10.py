# list = [1, 5, 6, 11, 2, 15]

# print("length of list:", len(list))

# print("1st element in list:", list[0])

# print("2nd element in list:", list[1])
# print("3rd element in list:", list[2])
# # # out of bounds
# print("7th element in list:", list[6])

# # using a loop
# i = 0
# while (i < len(list)):
#   print(list[i])
#   i = i + 1

# # # for loops
# for i in list:
#   print(i)



# # create sum function
# def sum(list):
#   sum = 0
#   for i in list:
#     sum = sum + i
#   return sum
# # print(sum([4, 3, 6])) # 13
# print(sum([1, 2, 3, 4, 5])) # 15

# list = []

# list.append(5)
# list.append(3)
# list.append(11)
# print(list)
# print(len(list))

# # create cumulativeSum function
# def cumulativeSum(list):
#   sum = 0
#   sumlist = []
#   for i in list:
#     sum = sum + i
#     sumlist.append(sum)
#   return sumlist

# # ex: the cumulative sum of [4, 3, 6] is [4, 7, 13]
# # print(cumulativeSum([4, 3, 6]))
# print(cumulativeSum([1, 2, 3, 4, 5])) # [1, 3, 6 , 10, 15]

# list can also contain strings
# list = ["hello", "world", "!"]

# write a report card creator
# ask for number of classes, name of each class, and grade
def report_card():
  classesCount = int(input("How many classes did you take? "))
  c = 0
  classnamelist = []
  classgradelist = []
  while (c<classesCount):
    classnamelist.append(input("what is the name of the class?"))
    classgradelist.append(input("what is your grade in this class?"))
    c = c + 1

  c = 0
  while (c < len(classnamelist)):


    print ("your grade in", classnamelist[c], "is", classgradelist[c])
    c = c + 1

report_card()