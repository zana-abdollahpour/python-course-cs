def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num
