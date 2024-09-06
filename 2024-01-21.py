# what do I do?
# def mystery(list):
#   s = 0
#   for i in list:
#     s = s + i
#   return s

# print(mystery([1, 1, 1])) # 3
# print(mystery([1, 2, 3, 4, 5])) # 1 3 6 10 15



# # what do I do?
# def mystery(list):
#   s = 0
#   newList = []
#   for i in list:
#     s = s + i
#     newList.append(s)
#   return newList

# print(mystery([1, 1, 1]))
# print(mystery([1, 2, 3, 4, 5]))


# # returns a list of all the even numbers in the input
# def findEvenNumbers(list):
  # newList = []
  # for i in list:
  #   if (i%2==0):
  #     newList.append(i)
  # return newList

# print(findEvenNumbers([1, 2, 3, 4, 5])) # [2, 4]
# print(findEvenNumbers([33, 75, 6, 11, 22])) # [6, 22]
# print(findEvenNumbers([1, 3, 5, 7, 9])) # []
# print(findEvenNumbers([2, 4, 6, 8, 10])) # [2, 4, 6, 8, 10]



# # returns a list of all the numbers in the list less than n
# def findSmallerThan(list, n):
#   newList = []
#   for i in list:
#     if (i < n):
#       newList.append(i)
#   return newList

# print(findSmallerThan([1, 2, 3, 4, 5], 3)) # [1, 2]
# print(findSmallerThan([10, 20, 30, 40, 50], 11)) # [10]
# print(findSmallerThan([20, 40, 3, 11, 15], 0)) # []
# print(findSmallerThan([89, 12, 1, 0, 45], 100)) # [89, 12, 1, 0, 45]


# # returns a list of all the numbers in the list that is divisible by n
# def findDivisibleBy(list, n):
#   newList = []
#   for i in list:
#     if (i%n==0):
#       newList.append(i)
#   return newList

# print(findDivisibleBy([2, 3, 5, 4, 7, 20], 2)) # [2, 4, 20]
# print(findDivisibleBy([11, 20, 30, 44, 50], 10)) # [20, 30, 50]



# # returns the biggest number in the list
# def findBiggest(list):
#   s=0
#   for i in list:
#     if ( s < i ):
#       s = i
#   return s

# print(findBiggest([5, 4, 3, 2, 1])) # 5
# print(findBiggest([1, 2, 3, 4, 5])) # 5
# print(findBiggest([6, 23, 544, 89, 1])) # 544




# returns a list of all the vowels in the word
# def findVowels(word):
#     newList = []
#     for c in word:
#       if (c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U"):
#         newList.append(c)
#     return newList


# print(findVowels("kelly")) # ["e"]
# print(findVowels("shuhua")) # ["u", "u", "a"]
# print(findVowels("potatoes")) # ["o", "a", "o", "e"]
# print(findVowels("serai")) # ["e", "a", "i"]
# print(findVowels("KELLY")) # ["E"]



# Write a function pig latin that takes in a single word, then converts the word to Pig Latin. To review, Pig Latin
# takes the first letter of a word, puts it at the end, and appends “ay”. The only exception is if the first letter is a
# vowel, in which case we keep it as it is and append “hay” to the end.
# E.g. “boot” => “ootbay”, and “image” => “imagehay”.
# It will be useful to define a list at the top of your code file called VOWELS. This way, you can check if a letter x is a
# vowel with the expression x in VOWELS. Remember - to get a word except for the first letter, you can use word[1:].
def pigLatin(word):
  # return word[0]
  c = word [0]
  if (c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U"):
    return word + "hay"
  else: 
    return word[1:] + c + "ay"


# print(pigLatin("boot"))#ootbay
# print(pigLatin("image"))#imagehay


# now for pig latin sentences!
def pigLatinSentence(sentence):

print(pigLatinSentence("what is your name")#hatway ishay ouryay amenay