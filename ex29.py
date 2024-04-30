# This code picks a random food item:
from random import choice  # DON'T CHANGE!
food = choice(["cheese pizza", "quiche", "morning bun",
              "gummy bear", "tea cake"])  # DON'T CHANGE!

bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# if (food in bakery_stock):
#     print(f"{bakery_stock[food]} left")
# else:
#     print("We don't make that here")

quantity = bakery_stock.get(food)
print(f"{quantity} left" if quantity else "We don't make that here")
