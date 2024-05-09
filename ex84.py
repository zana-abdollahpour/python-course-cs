def week():
    days = ["Monday", "Tuesday", "Wednessday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        yield day


w = week()
for day in w:
    print(day)
