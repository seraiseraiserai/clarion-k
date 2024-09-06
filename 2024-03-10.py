# # What do I do?
# def mystery():
#   print("hi")

# mystery()



# What do I do?
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



# # # What do I do?
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
#     i=i+1
#   return "bye"

# print(mystery())





# # What do I do?
# def mystery(list, n):
#     for i in list:
#       if (i < n):
#         return True
#     return False

# print(mystery([1, 2, 3, 4, 5], 3)) # True
# print(mystery([10, 20, 30, 40, 50], 3)) # false
# print(mystery([5, 4, 3, 2, 1], 3)) # T
# print(mystery([34, 2, 5, 76, 11], 1)) # F






# Let's build hangman!

# use me at the very end
# from random import randint
# def getSecretWord():
#     inFile = open( "words.txt", 'r')
#     secretWord_list = inFile.readline().split()
#     return secretWord_list[randint(0, len(secretWord_list))]


# Create isLetterInList, returns True if the letter is in the list
def isLetterInList(letter, list):
  for c in list:
    if(letter == c):
      return True
  return False

# print(isLetterInList("a", ["d", "c", "b", "a"])) # True
# print(isLetterInList("e", ["d", "c", "b", "a"])) # False
# print(isLetterInList("a", "banana")) # True
# print(isLetterInList("i", "watermellon")) # False



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
    if(not isLetterInList (c, lettersGuessed)):
      return False
  return True

# print(hasAllLettersBeenGuessed("apple", ["a", "e", "i", "l", "p"])) # True
# print(hasAllLettersBeenGuessed("watermellon", ["a", "e", "u", "s", "t", "l"])) # False
# print(hasAllLettersBeenGuessed("banana", [])) # False
# print(hasAllLettersBeenGuessed("banana", ["i", "u"])) # False





# Create isGameOver, returns True if the game is over
def isGameOver(secretWord, lettersGuessed, mistakes):

  return(mistakes == 6 or hasAllLettersBeenGuessed(secretWord, lettersGuessed))





print(isGameOver("apple", ["a", "e", "i", "l", "p"], 1)) # True
print(isGameOver("watermellon", ["a", "e", "u", "s", "t", "l"], 3)) # False
print(isGameOver("banana", ["i", "u", "q", "w", "t,", "y"], 6)) # True




# # Create printGameoutcome, it prints hangman one more time, tells me if I won or lost, and what the secretWord was
# def printGameoutcome(secretWord, lettersGuessed, mistakes):

# printGameoutcome("apple", ["a", "e", "i", "l", "p"], 1)
# printGameoutcome("watermellon", ["a", "e", "u", "s", "t", "l"], 3)
# printGameoutcome("banana", ["i", "u", "q", "w", "t,", "y"], 6)




# # Finally, build hangman
# secretWord = "claptrap"
# lettersGuessed = []
# mistakes = 0
# while(not isGameOver(secretWord, lettersGuessed, mistakes)):
#   printHangman(secretWord, lettersGuessed, mistakes)
#   letter = input("Please input a letter: ")

#   # If the player has already used letter, tell them.
#   # otherwise, play hangman

# printGameoutcome(secretWord, lettersGuessed, mistakes)

