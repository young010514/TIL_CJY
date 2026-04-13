n,m =map(int,input().split())
lst =list(map(int,input().split()))

Min = 21e8
used = [0] * n
result = []
def dfs(level,path):
    global Min, result

    if level == m :
        data = 1
        for x in range(m):
            data *= path[x]

        if Min > data :
            Min = data
            result = path[:]
            # print(result)

        return

    for i in range(n):
        if used[i] == 0:
            used[i] =1
            path.append(lst[i])
            dfs(level +1 , path)
            used[i] = 0
            path.pop()

dfs(0,[])

print(*sorted(result))