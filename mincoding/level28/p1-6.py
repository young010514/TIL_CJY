n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
for j in range(n):
    data =0
    for i in range(n):
        data += arr[i][j]
    if data == 0:
        root = j

def abc(idx):
    print(idx, end=' ')
    if sum(arr[idx]) == 0:
        return
    for i in range(n):
        if arr[idx][i] == 1:
            abc(i)

abc(root)

