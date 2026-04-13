import sys
sys.stdin = open("input_square.txt","r")

dts = [(0,1),(0,-1),(1,0),(-1,0)]
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result,cnt = 0,0
    def dfs(st,nx,ny, ncnt):
        global result,cnt
        if ncnt > cnt or (ncnt == cnt and result > st):
            cnt = ncnt
            result = st


        for i,j in dts :
            dx = nx + i
            dy = ny + j
            if dx < 0 or dy <0 or dx>n-1 or dy >n-1:continue
            if arr[dx][dy] - arr[nx][ny]== 1:
                dfs(st,dx,dy,ncnt+1)

    for i in range(n):
        for j in range(n):
            dfs(arr[i][j],i,j,1)


    print(f"#{tc} {result} {cnt}")

