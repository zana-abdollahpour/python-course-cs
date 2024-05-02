'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''


def triple_and_filter(nums):
    res = map(lambda x: x*3, filter(lambda num: num % 4 == 0, nums))
    return list(res)


print(triple_and_filter([1, 2, 3, 4]))
print(triple_and_filter([6, 8, 10, 12]))
