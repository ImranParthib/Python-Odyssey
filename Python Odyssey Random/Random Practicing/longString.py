for _ in range(int(input())):
    x = input()
    n = len(x)
    if n > 10:
        print(x[0] + str(n - 2) + x[n-1])
    else:
        print(x)