from random import random


def sing_hbd():
    print("happy birthday!")


sing_hbd()


def flip_coin():
    return "heads" if random() >= 0.5 else "tails"


print(flip_coin())


def add_up(a, b):
    return a+b


# Part 2

def calc_sum(*args):
    total = 0
    for num in args:
        total += num
    return total


def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print("{}'s favorite color is {}".format(person, color))


fav_colors(zana="gold", zhouan="green", giorno="pink")

print(calc_sum(*[1, 2, 3, 4, 5, 6]))
