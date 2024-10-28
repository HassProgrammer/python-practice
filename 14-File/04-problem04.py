# Search if the word "learning" exists in the file or not. 

with open("14-File/problem3.txt","r") as f:
    data = f.read()
    if data.find("learning") != -1:
        print("Found")
    else:
        print("Not found")