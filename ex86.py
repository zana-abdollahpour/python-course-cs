'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


def make_song(count=99, beverage="soda"):
    remaining = count
    for num in range(count-1):
        yield f"{remaining} bottles of {beverage} on the wall"
        remaining -= 1
    if remaining == 1:
        yield f"Only 1 bottle of {beverage} left!"
    yield f"No more {beverage}"

# Solution 2
# def make_song(verses=99, beverage="soda"):
#     for num in range(verses, -1, -1):
#         if num > 1:
#             yield "{} bottles of {} on the wall.".format(num, beverage)
#         elif num == 1:
#             yield "Only 1 bottle of {} left!".format(beverage)
#         else:
#             yield "No more {}!".format(beverage)


kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
