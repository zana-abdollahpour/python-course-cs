'''
partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


def isEven(num):
    return num % 2 == 0


# def partition(input_list, callback):
#     output_list = [[], []]
#     for item in input_list:
#         output_list[0].append(item) if callback(
#             item) else output_list[1].append(item)
#     return output_list


def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)], l]


print(partition([1, 2, 3, 4], isEven))
