# # what do I do?
# def mystery(list):
#   newList = []
#   for i in list:
#     if (i % 2 == 0):
#       newList.append(i)
#   return newList

# print(mystery([1, 2, 3, 4, 5])) # [2, 4]
# print(mystery([33, 75, 6, 11, 22])) # [6, 22]
# print(mystery([1, 3, 5, 7, 9])) # []

# what do I do?
def mystery(list):
  s = 0
  for i in list:
    if (s < i):
      s = i
  return s

print(mystery([1, 2, 3, 4, 5]))
print(mystery([6,7 23, 544, 89, 1]))


# # what do I do?
# def mystery(list):
#   s = 0
#   for i in list:
#     if (s < i):
#       s = i
#   return s

# print(mystery([1, 2, 3, 4, 5])) # 5
# print(mystery([6,7 23, 544, 89, 1])) # 544



# # reverse the string word
# def reverse(word):
#   w = ""
#   for c in word:
#     w = c + w
#   return w

# print(reverse("hello")) # olleh
# print(reverse("abcde")) # edcba
# print(reverse("I'm so mature")) #erutam os m'I



# Write a function pig latin that takes in a single word, then converts the word to Pig Latin. To review, Pig Latin
# takes the first letter of a word, puts it at the end, and appends “ay”. The only exception is if the first letter is a
# vowel, in which case we keep it as it is and append “hay” to the end.
# E.g. “boot” => “ootbay”, and “image” => “imagehay”.
def pigLatin(word):
  c = word [0]
  if (c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U"):
    return word + "hay"
  else: 
    return word[1:] + c + "ay"
  # w = ""
  # f = ""
  # i = 0
  # for c in word:
  #   isVowel =  c == "e" or c == "a" or c == "u" or c == "i" or c == "o"
  #   if (i == 0 and isVowel):
  #     return word + "hay"
  #   else:
  #     w = w + c
  #     f = c
  #   i = i + 1
  # return w + f + "ay"


# print(pigLatin("boot")) # ootbay
# print(pigLatin("image")) # imagehay


# now for pig latin sentences!
def pigLatinSentence(sentence):
  n = ""
  for word in sentence.split():
    n = n + pigLatin (word) + " "
  return n


print(pigLatinSentence("how was your day")) # hatway ishay ouryay amenay



# # returns a list of all the numbers that aren't in filteredNumbers
# def filterNumbers(numbers, filteredNumbers):
#   return []


# print(filteredNumbers([1, 2, 3, 4, 5], [2, 4]))
# print(filteredNumbers([4, 12, 8, 12, 3], [3, 12]))
# print(filteredNumbers([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
# print(filteredNumbers([1, 2, 3, 4, 5], [100, 200]))





# # returns a list of all the numbers that's in both numbersA and numbersB
# def intersection(numbersA, numbersB):
#   return []


# print(intersection([1, 2, 3, 4, 5], [3, 4, 5, 6]))
# print(intersection([4, 12, 8, 12, 3], [3, 12]))
# print(intersection([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
# print(intersection([1, 2, 3, 4, 5], [6, 7, 8, 9]))



# # Returns whether a word is a palindrome
# def isPalindrome(word):

# print(isPalindrome("madam"))
# print(isPalindrome("ferret"))
# print(isPalindrome("racecar"))
# print(isPalindrome("delicious"))


# # Returns whether a sentence is a palindrome
# # tools: sentence.lower()
# def isPaindromeSentence(sentence):

# print(isPaindromeSentence("A man, a plan, a canal, Panama"))
# print(isPaindromeSentence("I'm so mature"))
# print(isPaindromeSentence("Do Geese See God?"))
# print(isPaindromeSentence("A Santa Lived As A Devil at NASA"))
