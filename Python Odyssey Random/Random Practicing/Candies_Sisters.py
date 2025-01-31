for _ in range(int(input())):
    x = int(input())
    if x < 3:
        print(0)
    else:
        if x % 2 == 0:
            print((x // 2) - 1)
        else:
            print(x // 2)