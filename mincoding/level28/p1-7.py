n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for j in range(n):
    data = 0
    for i in range(n):
        if arr[i][j] == 1: data += 1
    if data ==0:
        root = j
        break


def abc(idx, path):
    path.append(idx)
    if sum(arr[idx]) ==0 :
        print(*path)
        return

    for i in range(n):
        if arr[idx][i] == 1:
            abc(i,path)
            path.pop()
abc(root,[])