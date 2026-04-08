import sys
sys.stdin =open("input_5.txt","r")

from collections import deque
def find(n,arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] =="2":
                return i,j
def bfs(sx,sy):
    dts = [(0,1),(0,-1),(1,0),(-1,0)]
    q= deque()
    q.append((sx,sy,0))
    while q:
        nx,ny,cnt = q.popleft()
        for i,j in dts:
            dx = nx+i
            dy = ny+j
            if dx <0 or dy<0 or dx> n-1 or dy >n-1:continue
            if arr[dx][dy] == "1":continue
            if arr[dx][dy] == "3": return cnt
            arr[dx][dy] ="1"
            q.append((dx,dy,cnt+1))
    return 0

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr= [list(input()) for _ in range(n)]
    sx,sy = find(n,arr)
    result = bfs(sx,sy)
    print(f"#{tc} {result}")