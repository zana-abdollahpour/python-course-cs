'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''


def repeat(pattern, num):
    s = ""
    for i in range(num):
        s += pattern
    return s


print(repeat('abc', 2))
