f = open('file.py')

# for line in open('file.py'):
#     print(line, end='')

while True:
    line = f.readline()
    if not line: break
    print(line, end='')