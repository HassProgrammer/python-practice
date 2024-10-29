# From a file containing numbers separated by comma, print the count of even numbers.
with open("14-File/06.txt", "r") as o:
    data = o.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if data[i] == ",":
            print(int(num))
            num = ""
        else:
            num = num + data[i]
        

 