import sys
sys.stdin = open("input_4.txt","r")

import heapq
def find(n,arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "X" :
                return i,j
def move(arr,sx,sy,k) : # 배열, 시작점, max 값
    dts = [(-1,0),(0,1),(1,0),(0,-1)]  # 위부터 오른족 방향으로 회전
    q = [(0,0,sx,sy,0,"")]  # 이동 수, 지금까지 벤 나무의 수, x,y, now direciton
    while q:
        ncnt,ntree,nx,ny,nd,prev = heapq.heappop(q)
        if arr[nx][ny] == "Y":
            return ncnt
        # 회전
        if prev != "R":
            heapq.heappush(q,(ncnt+1,ntree,nx,ny,(nd-1)%4,"L"))
        if prev != "L":
            heapq.heappush(q,(ncnt+1,ntree,nx,ny,(nd+1)%4, "R"))
        # 전진
        dx = nx + dts[nd][0]
        dy = ny + dts[nd][1]
        if dx <0 or dy < 0 or dx > n-1 or dy > n-1 : continue
        if arr[dx][dy] == "T" :
            if ntree + 1 <= k :
                heapq.heappush(q, (ncnt+1,ntree+1,dx,dy,nd,"T"))

        else: heapq.heappush(q, (ncnt+1,ntree,dx,dy,nd,"M"))

    return -1

T= int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    sx,sy = find(n,arr)   # 시작점 찾기


    result = move(arr,sx,sy,k)
    print(f"#{tc} {result}")