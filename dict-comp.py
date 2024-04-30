numbers = dict(first=1, second=2, third=3)
sq_nums = {key: val**2 for key, val in numbers.items()}
print(sq_nums)

print({num: num**2 for num in range(7)})

str1 = "ABCD"
str2 = "1234"
print({str1[i]: str2[i] for i in range(len(str1))})

print({num: ("even" if num % 2 == 0 else "odd") for num in range(10)})
