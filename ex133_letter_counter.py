'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''


def letter_counter(string):
    def inner(letter):
        return string.lower().count(letter.lower())

    return inner


def letter_counter2(s):
    letter_counter.val = s

    def inner(char):
        return len(list(c.lower() for c in letter_counter.val.lower() if c == char))
    return inner


# TEST
counter = letter_counter('Amazing')
print(counter('a'))  # 2
print(counter('m'))  # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i'))  # 2
print(counter2('t'))  # 1
