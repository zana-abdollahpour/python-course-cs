from keyword import iskeyword


def contains_keyword(*strings):
    return any(iskeyword(s) for s in strings)


print(contains_keyword("hello", "goodbye"))
print(contains_keyword("haha", "def"))
