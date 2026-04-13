import sys
sys.stdin = open("input_9.txt","r")

import heapq
dts=[(0,1),(0,-1),(1,0),(-1,0)]
def dijk(n,arr):
    result = [[9e4]*n for _ in range(n)]
    result[0][0] = 0
    q = [(0,0,0)]   # 값, x,y
    while q:
        now, nx,ny = heapq.heappop(q)
        if nx == n-1 and ny == n-1 :
            break
        for i,j in dts:
            dx = nx + i
            dy = ny + j
            if dx <0 or dy <0 or dx >n-1 or dy >n-1 : continue
            nxt = now + 1 + max(0,(arr[dx][dy] - arr[nx][ny]))
            if result[dx][dy] > nxt:
                result[dx][dy] = nxt
                heapq.heappush(q,(nxt,dx,dy))
    return result[n-1][n-1]
T=int(input())
for tc in range(1,1+T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = dijk(n,arr)
    print(f"#{tc} { ans}")