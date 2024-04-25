from random import randint

num = randint(1, 1000)

print(num, "is", "Even" if num % 2 == 0 else "Odd")
