def is_all_strings(inp): return all(type(item) == str for item in inp)


def is_all_strings2(lst):
    return all([type(l) == str for l in lst])
