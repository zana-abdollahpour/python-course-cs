demo = ["Elie", "Tim", "Matt"]
answer = "".join(word[0] for word in demo)
print(answer)

my_list = [1, 2, 3, 4, 5, 6]
answer2 = [num for num in my_list if num % 2 == 0]
print(answer2)
