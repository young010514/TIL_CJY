from collections import deque

directions = [(0,1),(0,-1),(1,0),(-1,0)]
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def bfs(x,y):
    q= deque()
    arr[x][y] = 0
    q.append((x,y))
    while q :
        nx,ny = q.popleft()
        for i,j in directions:
            dx = nx+i
            dy = ny+j
            if 0<= dx < n and 0<= dy < m :
                if arr[dx][dy] == 1:
                    arr[dx][dy] = 0
                    q.append((dx,dy))
cnt =0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs(i,j)
            cnt += 1
print(cnt)