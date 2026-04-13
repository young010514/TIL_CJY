import sys
sys.stdin = open("input_queen.txt","r")

import copy
from collections import deque
dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(1,1),(-1,1),(-1,-1)]

def chg_arr(arr,x,y, n):
    now = copy.deepcopy(arr)
    now[x][y] = 1
    for i,j in dirs:
        for d in range(1,n):
            dx = x + i*d
            dy = y + j * d
            if dx <0 or dy <0 or dx >n-1 or dy > n-1 : break
            now[dx][dy] = 1
    return now

def main(x,y,n):
    arr = [[0] * n for _ in range(n)]
    rst = 0
    q = deque()
    nxt = chg_arr(arr,0,y,n)
    q.append((0,y,nxt))   # 현재 좌표, 현재 arr
    while q:
        nx,ny,narr= q.popleft()
        if nx == n-1:
            rst += 1
            continue
        for j in range(n):
            if narr[nx+1][j] == 1: continue
            nxtarr = chg_arr(narr,nx+1,j,n)
            q.append((nx+1,j,nxtarr))

    return rst


T = int(input())
for tc in range(1,T+1):
    n = int(input())

    result = 0
    for j in range(n):
        result += main(0,j,n)

    print(f"#{tc} {result}")