'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''


def is_palindrome(input):
    left = 0
    right = len(input) - 1

    while left < right:
        if (input[left] != input[right]):
            return False
        left += 1
        right -= 1
    return True


def is_palindrome2(input):
    return input == input[::-1]


def is_palindrome3(input):
    stripped = input.replace(" ", "")
    return stripped == stripped[::-1]


print(is_palindrome('testing'))  # False
print(is_palindrome('tacocat'))  # True
print(is_palindrome('hannah'))  # True
print(is_palindrome('robert'))  # False
print(is_palindrome('amanaplanacanalpanama'))  # True
