# # what do I do?
# a = 5
# b = 1
# print(a + b)



# # what do I do?
# b = 3
# if (b + 3):
#   print("yayy")



# # what do I do?
# c = 14
# if (c == 14):
#   print("wooo")



# # what do I do?
# d = 1
# if (d == 2):
#    print("duck")
# else:
#    print("goose")



# # what do I do?
# import random

# def whatDoIDo():
#   n = (random.randint(0, 100))
#   print (n % 3 == 0)
#   print (n)

# whatDoIDo()
# whatDoIDo()
# whatDoIDo()



# write a rolling dice simulator
import random

def rollDice(sides, times):
  print("rolling", sides, "sided die", times, "times")
  n = 1
  while (n <= times):
    n = n + 1
    print (random.randint(1, sides))
    

rollDice(6, 3)
rollDice(4, 4)
rollDice(20, 10)

