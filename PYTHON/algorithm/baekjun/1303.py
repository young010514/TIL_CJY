from collections import deque
n,m = map(int,input().split())
arr = [list(input()) for _ in range(m)]
used = [[0] * n for _ in range(m)]
w,b = 0,0
dts = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(x,y):

    global w,b
    used[x][y] = 1
    q = deque()
    cnt = 1
    q.append((x,y))
    while q:
        nx,ny = q.popleft()
        for i,j in dts:
            dx = nx+i
            dy = ny+j
            if dx < 0 or dy <0 or dx > m-1 or dy > n-1 :continue
            if used[dx][dy] == 1 :continue
            if arr[dx][dy] != arr[x][y]:continue
            used[dx][dy] = 1
            cnt += 1
            q.append((dx,dy))
    if arr[x][y] == "W": w+= cnt**2
    else: b += cnt ** 2

for i in range(m):
    for j in range(n):
        if used[i][j] == 0 :
            bfs(i,j)
print(w,b)
