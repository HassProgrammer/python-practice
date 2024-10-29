# Print first 20 char
with open("14-File/07.txt", "r") as o:
    data = o.read(20)
    print(data) 
# Print lines
with open("14-File/07.txt", "r") as rl:
    data = rl.readlines()
    print(data) 

