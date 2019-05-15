import csv

with open("listcsv.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for name, email, contact in reader:
        if len(email) > 0:
            print(name, email, contact)

