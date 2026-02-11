P = int(input())
for _ in range(P):
    lst = list(map(int,input().split()))
    tc = lst[0]
    lst = lst[1:]
    result = []
    cnt= 0
    for i in lst:
        insert = -1
        for idx,j in enumerate(result):
            if j > i :
                insert = idx
                break
        if insert == -1:
            result.append(i)
        else:
            cnt += len(result[insert:])
            result = result[:insert] + [i] + result[insert:]

    print(f"{tc} {cnt}")