from random import randint

x = randint(-100, 100)
while x == 0:
    x = randint(-100, 100)

y = randint(-100, 100)
while y == 0:
    y = randint(-100, 100)


# if x > 0 and y > 0:
#     print(x, y, "both positive")
# elif x < 0 and y < 0:
#     print(x, y, "both negative")
# else:
#     pos = x if x > y else y
#     neg = x if pos == y else y
#     print(f"{pos} is positive and {neg} is negative")


if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")
