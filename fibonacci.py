# Normal
# def fib_list(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.append(b)
#         a, b = b, b+a
#     return nums


# Generator
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, y+x
        yield x
        count += 1
