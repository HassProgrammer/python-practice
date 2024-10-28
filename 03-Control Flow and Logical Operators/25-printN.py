def print_N(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n - 1 or j == i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  




print_N(5)