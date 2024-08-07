'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

# define mode below:


def mode(lst):
    freq = {}
    for item in lst:
        if freq.get(item) in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    freq_tuple = tuple((key, val) for key, val in freq.items())
    return max(freq_tuple, key=lambda x: x[1])[0]


def mode2(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]


print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))
