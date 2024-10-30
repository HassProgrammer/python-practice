import csv
try:
    csv_path = "14-File/09.csv"
    with open(csv_path, "r") as file:
        data = csv.reader(file)
        for line in data:
            print(line)
except FileNotFoundError:
    print("File not found!!")
except PermissionError:
    print("You do not have permission to read that file!!")