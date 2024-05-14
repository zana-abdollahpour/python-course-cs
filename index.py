from csv import reader, writer


with open("fighters.csv") as file:
    csv_reader = reader(file)
    # print(csv_reader)
    for fighter in csv_reader:
        pass
        # print(fighter)

with open("fighters.csv") as file:
    data = list(reader(file))
    for fighter in data:
        pass
        # print(fighter)
    for fighter in data:
        pass
        # print(fighter)


with open("fighters.csv") as file:
    data = DictReader(file)
    for fighter in data:
        pass
        # print(fighter)

with open("fighters.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["James", "Haul"])
