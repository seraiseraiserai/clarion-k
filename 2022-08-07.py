password = input("give me the password: ")
if (password != "password12345"):
    print("wrong password!")
else:
    print("correct!")

password = input("give me the password: ")
while (password != "password12345"):
    print("wrong password!")
    password = input("give me the password: ")
print("correct!")

number = 1
while (number <= 100):
    print(number)
    number = number + 1
odd = 1
while (odd <= 100):
    print(odd)
    odd = odd + 2
minus = 100
while (minus >= 0):
    print(minus)
    minus = minus - 1
even = 100
while (even >= 0):
    print(even)
    even = even - 2
