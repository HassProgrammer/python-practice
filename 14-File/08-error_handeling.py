file_path = "14-File/08"
try:
    with open(file_path, "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found!!")
except PermissionError:
    print("You do not have permission to read that file!!")