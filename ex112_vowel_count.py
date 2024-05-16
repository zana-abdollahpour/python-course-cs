'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''


def vowel_count(string):
    vowels = {"a": 0, "e": 0, "o": 0, "u": 0, "i": 0}
    for char in string.lower():
        if char in vowels:
            vowels[char] += 1
    return vowels


def vowel_count2(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}
