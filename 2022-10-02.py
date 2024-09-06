####### this is a function! #######
# def returnTheNumber(n):
#   return n

# print(returnTheNumber(17))
# print(returnTheNumber(5))
# print(6 + returnTheNumber(-7))

####### a function can do operations #######
# def addFive(n):
#   return n + 5

# print(addFive(3))
# print(addFive(-5))
# print(1 + addFive(1 + 2))

####### a function can take in multiple arguments #######
# def add(m, n):
#   return m + n

# print(add(5, 6))
# print(add(-4, 3))
# print(8 + add(9, 1))
# a = add(3, 4)
# print(7 + a)

####### assignment 1: create isDivisible #######
# def isDivisible(m, n):
#   return (m % n == 0):

  
# print(isDivisible(24, 2))
# print(isDivisible(35, 4))
# print(isDivisible(33, 33))
# print(isDivisible(43, 5))
# print(isDivisible(72, 8))


###### assignment 2: create notEqual #######
# def notEqual(m, n):
#   if (m == n ):
#     return False
#   else:
#     return True


# print(notEqual(3, 3)) # false
# print(notEqual(45, 87)) # true
# print(notEqual("hello", "hello")) # false


##### the random function #######
# ''import random

# n = 0
# while(n < 10):
#   print(random.randint(0, 5))
# #   n = n + 1
# ''

##### assignment 3: rock/paper/scissors AI #######
import random

#### work below

randomNumber = random.randint(1, 3)


if (randomNumber == 1): 
  computerMove = "rock"
elif (randomNumber == 2):
  computerMove = "scissors"
else:
  computerMove = "paper"



#### work above

player = input("what is your move? ")
print("computer throws out", computerMove)
if (player == "rock" and computerMove == "paper"):
    print("computer wins!")
elif (player == "scissors" and computerMove == "rock"):
    print("computer wins!")
elif (player == "paper" and computerMove == "scissors"):
    print("computer wins!")
elif (player == "paper" and computerMove == "rock"):
    print("you win!")
elif (player == "rock" and computerMove == "scissors"):
    print("you win!")
elif (player == "scissors" and computerMove == "paper"):
    print("you win!")
else:
    print("it is a tie!")
