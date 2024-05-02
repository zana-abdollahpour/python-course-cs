def interleave(str1, str2):
    return "".join(t[0]+t[1] for t in (zip(str1, str2)))
    # return ''.join(''.join(x) for x in (zip(str1, str2)))


print(interleave("abc", "xyz"))
