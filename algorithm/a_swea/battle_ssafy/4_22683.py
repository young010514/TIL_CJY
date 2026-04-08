import sys
sys.stdin = open("input_4.txt","r")

from collections import deque
def find(n,arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "X" :
                return i,j
def move(arr,sx,sy,k) : # 배열, 시작점, max 값
    dts = [(-1,0),(0,1),(1,0),(0,-1)]  # 위부터 오른족 방향으로 회전
    used = [[[[0] * (k+1) for _ in range(4)] for _ in range(n)] for _ in range(n)] # x,y,directions, trees
    q= deque()
    used[sx][sy][0][0] =1
    q.append((sx,sy,0,0,0)) # x,y,directions, trees, cnt
    while q:
        nx,ny,nd,nt,cnt = q.popleft()
        if arr[nx][ny] == "Y":
            return cnt
        # 왼쪽 오른족 회전
        if used[nx][ny][(nd-1)%4][nt] == 0 :
            used[nx][ny][(nd - 1) % 4][nt] =1
            q.append((nx,ny,(nd-1)%4, nt, cnt +1))
        if used[nx][ny][(nd+1)%4][nt] == 0 :
            used[nx][ny][(nd + 1) % 4][nt] =1
            q.append((nx,ny,(nd+1)%4, nt, cnt +1))

        # 전진
        dx = nx +dts[nd][0]
        dy = ny +dts[nd][1]
        if dx <0 or dy< 0 or dx >n-1 or dy>n-1:continue
        if arr[dx][dy] == "T":
            if nt + 1 >k :continue


            if used[dx][dy][nd][nt+1] == 1:continue
            used[dx][dy][nd][nt+1] =1
            q.append((dx,dy,nd,nt+1,cnt+1))
        elif used[dx][dy][nd][nt] == 0:
            used[dx][dy][nd][nt] =1
            q.append((dx,dy,nd,nt,cnt+1))
    return -1


T= int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    sx,sy = find(n,arr)   # 시작점 찾기


    result = move(arr,sx,sy,k)
    print(f"#{tc} {result}")