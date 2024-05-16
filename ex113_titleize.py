'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''


def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))


def titleize2(string):
    s = ""
    for word in string.split(" "):
        s += word[0].upper() + word[1:] + " "
    return s
