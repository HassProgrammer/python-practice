file_path = "14-File/08"
try:
    with open(file_path, "r") as file:
        data = file.read()
        print(data)
except:
    print("File not found!!")