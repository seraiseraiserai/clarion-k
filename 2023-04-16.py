# what do I do?
# list = []
# i = 0
# while(i <= 100):
#    if (i % 2 == 1):
#     list.append(i)
#    i = i + 1
# print(list)

# # what do I do?
# def mystery(list):
#   s = 0
#   output = []
#   for l in list:
#    s = s + l
#    output.append(s)
#   return output
  
# print(mystery([5, 4, 3, 2, 1]))
# print(mystery([11, 11, 11]))

# list can also contain strings
# list = ["hello", "world", "!"]
# print(list)

# # create a list of ["ah", "ahh", "ahhh", "ahhhh", ...] based on an input of how many h's

hCount = int(input("How many h? "))

x = 0
h = "ah"
list = []
while ( x <= hCount):
  list.append(h)
  x = x + 1
  h = h + "h"
print(list)


# def ahhh(hCount):
#   output = ["ah"]
#   while ( h == 15):
#    return output

# hCount = int(input("How many h? "))
# print(ahhh(hCount))


# # write a report card creator
# # ask for number of classes, name of each class, and grade. Then print them out
# def report_card():
#   classesCount = int(input("How many classes did you take? "))

# report_card()


# # for loops can also be used to loop a text
# text = "hello world!"
# for letter in text:
#   print(letter)

# # you can also use a while loop
# text = "hello world!"
# i = 0
# while(i < len(text)):
#   print(text[i])
#   i = i + 1

# # return all the vowels of the text in a list
# def findVowels(text):
#   vowels = []
#   return vowels

# findVowels("hello world!")
# findVowels("what is your favorite color?")

