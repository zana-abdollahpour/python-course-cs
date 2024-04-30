'''
last_element([1,2,3]) # 3
last_element([]) # None
'''


def last_element(input_list):
    length = len(input_list)
    return None if length == 0 else input_list[-1]


print(last_element([1, 2, 3]))
