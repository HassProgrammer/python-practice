def show(n):
    if n == 0:
        return
    else:
        print(n)
        show(n-1)
show(5)