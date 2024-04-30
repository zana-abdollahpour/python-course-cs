'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''


def multiply_even_numbers(nums):
    result = 1
    for num in nums:
        if num % 2 == 0:
            result *= num
    return result


print(multiply_even_numbers([2, 3, 4, 5, 6]))
