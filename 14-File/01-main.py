#File open
f = open("14-File/demo.txt", "r")
data = f.read()
print(data)
f.close()

# specific character read
f2 = open('14-File/demo.txt', 'r')
data2 = f2.read(6)
print(data2)
f2.close()

# reads one line at a time
f3 = open("14-File/demo.txt", "r")
line1 = f3.readline()
print(line1)
f3.close()

# reads line by line at a time
f4 = open("14-File/demo.txt", "r")
line1 = f4.readline()
line2 = f4.readline()
print(line1)
print(line2)

# write or overwrite data
f5 = open("14-File/demo2.txt","w")
f5.write("Why so serious!!")
f5.close()

# append data
f6 = open("14-File/demo2.txt","a")
f6.write("Put on a happy face.")
f6.write("\nHaHahaaaha!")
f6.close()

# # create a new file using code
# f7 = open("new file.txt", "w")
# f7.write()
# f7.close