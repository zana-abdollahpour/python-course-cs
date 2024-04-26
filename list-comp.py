test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = [(num*2 if num < 5 else num*10) for num in test_list]
# --> [2, 4, 6, 8, 50, 60, 70, 80, 90]

res = [num for num in res if num < 50]
# --> [2, 4, 6, 8]

with_vowels = "This is so much fun!"
no_vowels = "".join(char for char in with_vowels if char not in "aeiou")
# --> "Ths s s mch fn!"

print(no_vowels)
