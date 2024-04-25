start = 0
end = 10

while start < end + 1:
    print(" " * (end + 1 - start) * 2, "\U0001f500" * ((start * 2) + 1))
    start = start + 1

print("\n")

inp = input("Say something: ")
while inp.lower() != "stop copying me":
    inp = input(inp + "\n")
print("*** UGH! FINE! YOU WIN! ***")
