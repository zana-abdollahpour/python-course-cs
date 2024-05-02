# square = lambda num : num*num
def square(num): return num*num


users = []  # list of users, not written

usernames = list(map(lambda user: user.username.upper(),
                 filter(lambda user: not user["tweets"], users)))


res = "Hi Jotaro"[::-1]
print(res)

print(round(10.6))
