from csv import reader, writer, DictWriter

with open("fighters.csv") as file:
    csv_reader = reader(file)
    # fighters = [[s.upper() for s in row] for row in csv_reader]
    with open("screaming_fighters.csv", "w") as file:
        csv_writer = writer(file)
        # for fighter in fighters:
        for fighter in csv_reader:
            # csv_writer.writerow(fighter)
            csv_writer.writerow(s.upper() for s in fighter)
