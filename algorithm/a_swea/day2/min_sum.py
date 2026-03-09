import sys
sys.stdin = open("input_minsum.txt","r")

from collections import deque
directions = [(0,1),(0,-1),(1,0),(-1,0)]
def main(n,arr):
    used = [[0]*n for _ in range(n)]
    result = 2e6
    q = deque()
    used[0][0] = 1
    q.append((0,0,arr[0][0], used))   # x,y,sum, path
    while q :

        nx,ny,nsum,nused = q.popleft()

        if nx == n-1 and ny ==n -1 :
            if result > nsum : result = nsum
        for i,j in directions:
            dx = nx + i
            dy = ny + j
            if dx < 0 or dy <0 or dx > n-1 or dy >n-1 : continue
            if nused[dx][dy] == 1: continue
            nxt = [row[:] for row in nused]
            nxt[dx][dy] = 1
            q.append((dx,dy,nsum + arr[dx][dy], nxt))
    return result


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    rst = main(n,arr)
    print(f"#{tc} {rst}")
