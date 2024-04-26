list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
answer = [num for num in list1 if num in list2]
print(answer)


demo = ["Elie", "Tim", "Matt"]
answer2 = [[word.lower()[::-1]] for word in demo]
print(answer2)
