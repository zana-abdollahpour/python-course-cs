# def remove_negatives(l): return [num for num in l if num >= 0]


def remove_negatives(l): return list(filter(lambda num: num >= 0, l))
