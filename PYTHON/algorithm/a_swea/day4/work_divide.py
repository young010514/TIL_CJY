import sys
sys.stdin = open("input_work.txt","r")


T = int(input())
for tc in range(1,T+1):

    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    used = [0] * n
    result = 0
    def dfs(x,data):
        global result
        if data < result : return
        if x == n:
            if result < data : result = data
            return
        for i in range(n):
            if used[i] == 1: continue
            if arr[x][i] == 0 : continue
            used[i] = 1
            dfs(x+1, data * (arr[x][i]/100))
            used[i] = 0
    dfs(0,100)
    print(f"#{tc} {result :.6f}")