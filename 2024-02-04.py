# # what do I do?
# def mystery(word):
#   w = ""
#   for c in word:
#     w = c + w
#   return w

# print(mystery("hello"))
# print(mystery("abcde"))
# print(mystery("I'm so mature"))



# Write a function pig latin that takes in a single word, then converts the word to Pig Latin. To review, Pig Latin
# takes the first letter of a word, puts it at the end, and appends “ay”. The only exception is if the first letter is a
# vowel, in which case we keep it as it is and append “hay” to the end.
# E.g. “boot” => “ootbay”, and “image” => “imagehay”.
# vowel with the expression x in VOWELS. Remember - to get a word except for the first letter, you can use word[1:].
def pigLatin(word):
  c = word [0]
  if (c == "a" or c == "A" or c == "e" or c == "E" or c == "i" or c == "I" or c == "u" or c == "U" or c == "o" or c == "O"):
    return word + "hay"
  else:
    return word [1:] + c + "ay"


# print(pigLatin("boot")) # ootbay
# print(pigLatin("image")) # imagehay


# # now for pig latin sentences!
# def pigLatinSentence(sentence):
#   n = ""
#   for word in sentence.split():
#     n = n + pigLatin(word) + " "
#   return n


# print(pigLatinSentence("how was your day")) # hatway ishay ouryay amenay

def isInList(n, list):
  for i in list:
    if (n == i):
      return True
  return False

# print(isInList(3, [1, 2, 3, 4, 5])) # True
# print(isInList(3, [1, 2, 4])) # False

# returns a list of all the numbers that aren't in filteredNumbers
def filterNumbers(numbers, filteredNumbers):
  newlist = []
  for i in numbers:
    if (not isInList(i, filteredNumbers)): 
      newlist.append(i)
  return newlist


# print(filterNumbers([1, 2, 3, 4, 5], [2, 4])) # [1, 3, 5]
# print(filterNumbers([4, 12, 8, 12, 3], [3, 12])) # [4, 8]
# print(filterNumbers([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])) # []
# print(filterNumbers([1, 2, 3, 4, 5], [100, 200])) # [1, 2, 3, 4, 5]





# returns a list of all the numbers that's in both numbersA and numbersB
def intersection(numbersA, numbersB):
  newlist = []
  for i in numbersA:
    if ( isInList(i , numbersB)): 
      newlist.append(i)
  return newlist


print(intersection([1, 2, 3, 4, 5], [3, 4, 5, 6])) # [3, 4, 5]
print(intersection([4, 12, 8, 12, 3], [3, 12])) # []
print(intersection([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
print(intersection([1, 2, 3, 4, 5], [6, 7, 8, 9]))



# # Returns whether a word is a palindrome
# def isPalindrome(word):

# print(isPalindrome("madam"))
# print(isPalindrome("ferret"))
# print(isPalindrome("racecar"))
# print(isPalindrome("delicious"))


# # Returns whether a sentence is a palindrome
# # tools: sentence.lower(), sentence.replace()
# def isPaindromeSentence(sentence):

# print(isPaindromeSentence("A man, a plan, a canal, Panama"))
# print(isPaindromeSentence("I'm so mature"))
# print(isPaindromeSentence("Do Geese See God?"))
# print(isPaindromeSentence("A Santa Lived As A Devil at NASA"))
