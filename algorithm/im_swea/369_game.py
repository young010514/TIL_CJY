N = int(input())
for i in range(1,N+1):
    lst = list(str(i))

    cnt = lst.count("3") + lst.count("6") + lst.count("9")

    if cnt :
        print("-"*cnt, end=' ')
    else:
        print(i, end=' ')