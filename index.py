cat = {"name": "blue"}
cat2 = dict(weight=45, size=12, name="Andrei")

# print(cat)
# print(cat2)

# print(cat["name"])
# print(cat2.values())
# print(cat2.keys())
# print(cat2.items())

# for k, v in cat2.items():
#     print(f"key is {k}, and value is {v}")

# if "name" in cat2:
#     print(cat2["name"])

cat3 = cat2.copy()

# cat4 = {}.fromkeys("Ab bas", {"name": "Jones"})
# cat5 = dict.fromkeys(range(4), {"name": "Jones"})
# print(cat5)
# print(cat4[" "])
# print(cat5.get(1))
# print(cat5.get(8))

print(cat3.pop("name"), "<-->", cat3)

# print(cat2.popitem())

cat.update(cat2)
print(cat)
