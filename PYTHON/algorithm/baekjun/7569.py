m,n,h = map(int,input().split())
arr = []
for i in range(h):
    arr.append([list(map(int,input().split())) for _ in range(n)])
from collections import deque
dts = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
q = deque()

result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                    q.append((i,j,k,0))   # nh, nn, nm, time

while q :
    nh,nx,ny,level = q.popleft()
    if level > result : result = level
    for i,j,k in dts:
        dh = nh + i
        dx = nx + j
        dy = ny + k
        if dh < 0 or dh > h-1 or dx <0 or dy <0 or dx >n-1 or dy >m-1 : continue
        if arr[dh][dx][dy] == -1 : continue
        if arr[dh][dx][dy] == 1 :continue
        arr[dh][dx][dy] = 1
        q.append((dh,dx,dy,level + 1))
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 0 :
                result = -1
                break
print(result)

