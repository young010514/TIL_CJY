from collections import deque
n,m = map(int,input().split())
arr = [input() for _ in range(n)]

dts = [(0,1),(0,-1),(1,0),(-1,0)]
def cnt(x,y):
    global nodes, result
    if (x,y) in nodes: return
    q = deque()
    used = [[-1] * m for _ in range(n)]
    q.append((x,y))
    used[x][y] = 0
    while q:
        nx,ny = q.popleft()
        for i,j in dts:
            dx = nx + i
            dy = ny + j
            if dx <0 or dy< 0 or dx > n-1 or dy >m-1:continue
            if used[dx][dy] != -1 :continue
            if arr[dx][dy] == "W" : continue
            used[dx][dy] = used[nx][ny] +1
            q.append((dx,dy))
    Max =0
    edx =  0
    for i in range(n):
        for j in range(m):
            if used[i][j] > Max :
                Max = used[i][j]
                edx = (i,j)
    if result < Max :
        result = Max
        nodes = [(x,y), edx]


nodes = []
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L" :
            cnt(i,j)
print(result)