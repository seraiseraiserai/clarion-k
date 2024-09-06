# # what do I do?
# def mystery():
#   i = 1
#   while (i <= 3):
#     j = 1
#     while(j <= 2):
#       print(i * j)
#       j = j + 1
#     i = i + 1

# # mystery()

# # what do I do?
# def mystery():
#   i = 1
#   j = 1
#   while (i <= 3):
#     while(j <= 2):
#       print(i * j)
#       j = j + 1
#     i = i + 1

# mystery()

# # what do I do?
# def mystery():
#   listA = [1, 2, 3]
#   listB = [5, 6, 7]
#   for a in listA:
#     for b in listB:
#       print(a * b)

# mystery()



# # Returns whether a word is a palindrome
def isPalindrome(word):
  w=""
  for c in word:
    w = c + w
  return word == w


# print(isPalindrome("abcde"))
# print(isPalindrome("madam")) # true
# print(isPalindrome("ferret")) # false
# print(isPalindrome("racecar")) # true
# print(isPalindrome("delicious")) # false



# Returns whether a sentence is a palindrome
# tools: sentence.lower(), sentence.replace()
def isPalindromeSentence(sentence):
  newSentence = sentence.replace(" ", "")
  newSentence = newSentence.replace(",", "")
  newSentence = newSentence.lower()
  newSentence = newSentence.replace("?", "")
  return isPalindrome(newSentence)

print(isPalindromeSentence("A man, a plan, a canal, Panama")) # true
print(isPalindromeSentence("I'm so mature")) # false
print(isPalindromeSentence("Do Geese See God?")) # true
print(isPalindromeSentence("A Santa Lived As A Devil at NASA")) # true




# # returns a list of all the numbers that's in both numbersA and numbersB
# def intersection(numbersA, numbersB):

# print(intersection([1, 2, 3, 4, 5], [3, 4, 5, 6]))
# print(intersection([4, 12, 8, 12, 3], [3, 12]))
# print(intersection([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
# print(intersection([1, 2, 3, 4, 5], [6, 7, 8, 9]))


# returns a list of all the numbers that aren't in filteredNumbers
# def filterNumbers(numbers, filteredNumbers):

# print(filterNumbers([1, 2, 3, 4, 5], [2, 4]))
# print(filterNumbers([4, 12, 8, 12, 3], [3, 12]))
# print(filterNumbers([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
# print(filterNumbers([1, 2, 3, 4, 5], [100, 200]))


