'''
primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''


def next_prime():
    num = 2
    all_primes = set()
    while True:
        for prime in all_primes:
            if num % prime == 0:
                break
        else:
            all_primes.add(num)
            yield num
        num += num % 2 + 1
