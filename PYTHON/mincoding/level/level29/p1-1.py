n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]


def abc(idx):
    print(idx,end=' ')
    if sum(arr[idx]) == 0:
        return
    for i in range(n):
        if arr[idx][i] == 1:
            abc(i)
abc(0)