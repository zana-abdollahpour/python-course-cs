from csv import DictWriter

with open("dogs.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Iggy",
        "Breed": "Gamal",
        "Age": 4,
    })
