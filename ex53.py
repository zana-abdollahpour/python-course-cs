'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''


def capitalize(word):
    return word[0].upper() + word[1:].lower()


print(capitalize("tim"))
print(capitalize("matt"))
