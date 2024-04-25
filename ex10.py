from random import choice

food = choice(["apple", "grape", "bacon", "steak", "worm", "dirt"])


if food == "apple" or food == "grape":
    print(food, "fruit")

if food == "bacon" or food == "steak":
    print(food, "meat")

if food == "worm" or food == "dirt":
    print(food, "yuck")
