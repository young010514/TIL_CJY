import sys
sys.stdin = open("input_arr_min.txt","r")

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]
    Min = 2e8
    used = [0] * n
    def dfs(x,Sum) :
        global Min
        if Sum > Min : return
        if x == n:
            Min = min(Sum,Min)
            return

        for i in range(n):
            if not used[i] :
                used[i]  =1
                dfs(x+1, Sum + lst[x][i])
                used[i] = 0

    dfs(0, 0)
    print(f"#{tc} {Min}")