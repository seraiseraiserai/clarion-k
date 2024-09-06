# what do I do?
# a = 1
# while (a <= 100):
#     print(a)
#     a = a + 2

# # what do I do?
# i = 0
# while (i <= 100):
#     if (i % 2 == 0):
#         print(str(i) + " is even!")
#     else:
#         print(str(i) + " is odd!")
#     i = i + 1

# what do I do?
# print("a" + "a" + "a" + "a" + "a")

# what do I do?
# output = ""
# i = 0
# while (i < 20):
#     output = output + "a"
#     i = i + 1
# print(output)

# what do I do?
# print(" o ")
# print("/|\\")
# print("/ \\")

# import time
# import os

# # what do I do?
# x = 0
# spaces = ""
# while (x < 100):
#     os.system("clear")
#     if (x % 2 == 0):
#         print(spaces + " o ")
#         print(spaces + "/|\\")
#         print(spaces + "/ \\")
#     else:
#         print(spaces + " o ")
#         print(spaces + "/|\\")
#         print(spaces + " | ")
#     time.sleep(0.1)
#     spaces = spaces + " "
#     x = x + 1

size = int(input("how big of a box: "))

y = 0
while (y < size):
    output = ""
    x = 0
    while (x < size):
        output = output + "#"
        x = x + 1
    print(output)
    y = y + 1
