n = int(input())
arr = [input() for _ in range(n)]

dts = [(0,1),(0,-1),(1,0),(-1,0)]

from collections import deque
q1, q2 = deque(), deque()

def bfs(x,y) :
    q= deque()
    q.append((x,y))
    used[x][y] = 1
    color = arr[x][y]
    while q :
        nx,ny = q.popleft()
        for i,j in dts:
            dx = nx + i
            dy = ny + j
            if dx <0 or dy< 0 or dx > n-1 or dy > n-1:continue
            if used[dx][dy] == 1: continue
            if arr[dx][dy] == color :
                used[dx][dy] = 1
                q.append((dx,dy))


def bfs1(x, y):
    q = deque()
    q.append((x, y))
    used1[x][y] = 1


    while q:
        nx, ny = q.popleft()
        for i, j in dts:
            dx = nx + i
            dy = ny + j
            if dx < 0 or dy < 0 or dx > n - 1 or dy > n-1:continue
            if used1[dx][dy] == 1: continue
            if (arr[dx][dy] in ["R","G"] and arr[x][y] in ["R","G"] ) or arr[dx][dy] == arr[x][y]:
                used1[dx][dy] = 1
                q.append((dx, dy))


rst1,rst2 = 0,0
used=[[0] * n for _ in range(n)]
used1=[[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if used[i][j]== 0 :
            bfs(i,j)
            rst1 += 1
        if used1[i][j] ==0:
            bfs1(i,j)
            rst2+= 1
print(rst1,rst2)

