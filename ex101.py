'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

from csv import reader


def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)


print(find_user("Colt", "Steele"))
print(find_user("Alan", "Turing"))
print(find_user("Not", "Here"))
