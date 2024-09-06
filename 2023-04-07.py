# # What do I do?
# x = 12
# y = 7
# z = 28
# s = "banana"

# print(x < 14)#true
# print(not (x % 2 < 1))#false
# print(x < y or x < z)#true
# print(x < y and x < z)#false
# print(x > y and x < z)#true
# print(len(s) == y)#false
# print(not s == "banana" or x * y != z)#true
# print(not (s == "banana" or x * y != z))#false


# # What do I do?
# def mystery():
#   print("hi")

# mystery()



# # What do I do?
# def mystery():
#   print("hi")

# print(mystery())


# # What do I do?
# def mystery():
#   return "hi"

# print(mystery())



# # What do I do?
# def mystery():
#   return "hi"

# mystery()


# # What do I do?
# def mystery():
#   i = 0
#   while (i < 5):
#     print ("hi")
#     i = i + 1

# mystery()


# # What do I do?
# def mystery():
#   i = 0
#   while (i < 5):
#     return "hi"
#     i = i + 1

# print(mystery())



# # What do I do?
# def mystery():
#   i = 0
#   while (i < 5):
#     return "hi"
#     i = i + 1
#     print("yay!")

# print(mystery())





# # What do I do?
# def mystery():
#   i = 0
#   while (i < 5):
#     print("hi")
#     i = i + 1
#   return "bye"

# print(mystery())





# # what do I do?
# def mysteryFunction(a):
#   print(a)

# a = 5
# mysteryFunction(a)


# # what do I do?
# def mysteryFunction(a):
#   a = 7
#   print(a)

# a = 5
# mysteryFunction(a)


# # what do I do?
# def mysteryFunction(a):
#   return 7

# a = 5

# print(mysteryFunction(a))



# # what do I do?
# a = 5
# def mysteryFunction(a):
#   a = 7

# mysteryFunction(a)
# print(a)



# # what do I do?
# a = 5
# def mysteryFunction(a):
#   a = 7
#   print(a)

# mysteryFunction(a)
# print(a)
# mysteryFunction(a)



# # What do I do?
# def mystery(list, n):
#     for i in list:
#       if (i < n):
#         return True
#     return False

# print(mystery([1, 2, 3, 4, 5], 3)) # True
# print(mystery([10, 20, 30, 40, 50], 3)) # False
# print(mystery([5, 4, 3, 2, 1], 3)) # True
# print(mystery([34, 2, 5, 76, 11], 1)) # False



# Let's build hangman!

# use me at the very end
from random import randint
def getSecretWord():
    inFile = open( "words.txt", 'r')
    secretWord_list = inFile.readline().split()
    return secretWord_list[randint(0, len(secretWord_list))]


# Create isLetterInList, returns True if the letter is in the list
def isLetterInList(letter, list):
  for c in list:
    if(letter == c):
      return True
  return False

# print(isLetterInList("a", ["d", "c", "b", "a"])) # T
# print(isLetterInList("e", ["d", "c", "b", "a"])) # F
# print(isLetterInList("a", "banana")) # T
# print(isLetterInList("i", "watermellon")) # F



# Create printWordProgress, that prints all the correctly guessed letters in their correct positions
def printWordProgress(secretWord, lettersGuessed):
  progress = ""
  for c in secretWord:
    if(isLetterInList (c, lettersGuessed)):
      progress = progress + c
    else:
      progress = progress + "-"
  print(progress)

# printWordProgress("banana", ["a", "b"]) # ba-a-a
# printWordProgress("watermellon", ["i", "o"]) # -------o-
# printWordProgress("apple", ["i", "o"]) # -----
# printWordProgress("apple", ["a", "l", "e", "p"]) # apple





# # Create printHangman, that prints the stick figure, the word progress, and all the letters guessed so far
def printHangman(secretWord, lettersGuessed, mistakes):
  if (mistakes == 6):
    print('''
  _____
  |   |
  |   o
  |  -|-
  |  / \\
  |
  -------
      ''')
  if (mistakes == 1):
      print('''
    _____
    |   |
    |   o
    |
    |  
    |
    -------
        ''')
  if (mistakes == 2):
      print('''
    _____
    |   |
    |   o
    |   |
    |  
    |
    -------
        ''')
  if (mistakes == 3):
      print('''
    _____
    |   |
    |   o
    |  -|
    |  
    |
    -------
        ''')
  if (mistakes == 4):
      print('''
    _____
    |   |
    |   o
    |  -|-
    |  
    |
    -------
        ''')
  if (mistakes == 5):
      print('''
    _____
    |   |
    |   o
    |  -|-
    |  /
    |
    -------
        ''')
  if (mistakes == 0):
      print('''
    _____
    |   |
    |   
    |  
    |  
    |
    -------
        ''')

  printWordProgress(secretWord, lettersGuessed)
# printHangman("watermellon", ["a", "e", "u", "s", "t", "l"], 3)
# printHangman("apple", [], 0)




# Create hasAllLettersBeenGuessed, returns true if all the letters in secretWord has been guessed
def hasAllLettersBeenGuessed(secretWord, lettersGuessed):
  for c in secretWord:
    if (not isLetterInList (c, lettersGuessed)):
      return False
  return True


# print(hasAllLettersBeenGuessed("apple", ["a", "e", "i", "l", "p"])) # T
# print(hasAllLettersBeenGuessed("watermellon", ["a", "e", "u", "s", "t", "l"])) # F
# print(hasAllLettersBeenGuessed("banana", [])) # F
# print(hasAllLettersBeenGuessed("banana", ["i", "u"])) # F





# Create isGameOver, returns True if the game is over
def isGameOver(secretWord, lettersGuessed, mistakes):
  if (hasAllLettersBeenGuessed(secretWord, lettersGuessed) or mistakes == 6):
    return True
  return False



print(isGameOver("apple", ["a", "e", "i", "l", "p"], 1)) # True
print(isGameOver("watermellon", ["a", "e", "u", "s", "t", "l"], 3)) # False
print(isGameOver("banana", ["i", "u", "q", "w", "t,", "y"], 6)) # True




# Create printGameoutcome, it prints hangman one more time, tells me if I won or lost, and what the secretWord was
def printGameOutcome(secretWord, lettersGuessed, mistakes):
  printHangman(secretWord, lettersGuessed, mistakes)
  if (hasAllLettersBeenGuessed(secretWord, lettersGuessed) and mistakes < 6 ):
    print("You've Won!")
  else:
    print("game over!")
    print("the word was", secretWord)

# printGameOutcome("apple", ["a", "e", "i", "l", "p"], 1)
# printGameOutcome("watermellon", ["a", "e", "u", "s", "t", "l"], 3)
# printGameOutcome("banana", ["i", "u", "q", "w", "t,", "y"], 6)




# # Finally, build hangman
secretWord = getSecretWord()
lettersGuessed = []
mistakes = 0

# use isGameOver, printHangman, printGameoutcome
# while the game is not over, print the game state
# then ask for input
while(not isGameOver(secretWord, lettersGuessed, mistakes)):
  printHangman( secretWord, lettersGuessed, mistakes)
  letter = input("Please input a letter: ")
  if(isLetterInList(letter, lettersGuessed)):
    print("you've already guessed this letter")
  elif(isLetterInList(letter, secretWord)):
    lettersGuessed.append(letter)
  else: 
    mistakes = mistakes + 1
    lettersGuessed.append(letter)
printGameOutcome(secretWord, lettersGuessed, mistakes)



  # If the player has already used letter, tell them.
  # otherwise, play hangman

# when the game is over, print the game outcome

