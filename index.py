file = open("intro.txt")
data = file.read()


with open("intro.txt") as f:
    print(f.closed)
    print(f.read())

print(f.closed)
