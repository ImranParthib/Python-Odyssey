def Highest_Position():
    j = 0
    loc = 0
    for i in range(100):
        n = int(input())
        if (n > j):
            j = n
            loc = i
    print(j)
    print(loc + 1)


Highest_Position()         
