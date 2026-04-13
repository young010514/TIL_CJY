m,n=map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

from collections import deque
dts = [(0,1),(0,-1),(1,0),(-1,0)]
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 :
            q.append((i,j,0))   # x,y, day
result = 0
while q :
    nx,ny,level = q.popleft()
    if level > result : result = level
    for i,j in dts:
        dx = nx + i
        dy = ny + j
        if dx <0 or dy <0 or dx >n-1 or dy >m-1 : continue
        if arr[dx][dy] == -1 : continue
        if arr[dx][dy] == 1 :continue
        arr[dx][dy] = 1
        q.append((dx,dy,level + 1))
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 :
            result = -1
            break
print(result)
