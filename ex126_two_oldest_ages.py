'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''


def two_oldest_ages(lst):
    return sorted(lst)[-2:]
    # sorted_lst = sorted(lst)
    # return (sorted_lst[-2], sorted_lst[-1])


print(two_oldest_ages([1, 2, 10, 8]))
