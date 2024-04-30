def contains_purple(*args):
    return args.count("purple") >= 1


def contains_blue(*args):
    if "blue" in args:
        return True
    return False
