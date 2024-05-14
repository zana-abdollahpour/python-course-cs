'''
print_users() # None
# prints to the console:
# Colt Steele
'''

from csv import DictReader


def print_users(file_name):
    with open(file_name) as file:
        csv_reader = DictReader(file)
        for person in csv_reader:
            print(person["First Name"], person["Last Name"])


print_users("users.csv")
