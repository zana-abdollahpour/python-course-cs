
# flesh out intersection pleaseeeee


def intersection(l1, l2):
    return [val for val in l1 if val in l2]


def intersection_adv(list1, list2):
    return [val for val in set(list1) & set(list2)]


print(intersection_adv([1, 2, 3], [2, 3, 4, 5, 6]))
