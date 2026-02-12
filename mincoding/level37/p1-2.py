from collections import deque

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
a,b = map(int,input().split())


directions = [(-1,0),(1,0),(0,1),(0,-1)]
result = [[0] * m for _ in range(n)]
q = deque()
arr[a][b] = 1
q.append([0,a,b])
while q :
    cnt, x,y= q.popleft()

    for i,j in directions:
        dx = x + i
        dy = y + j
        if dx < 0 or dy < 0 or dx >= n or dy >= m:continue
        if arr[dx][dy] == 1: continue

        result[dx][dy] = cnt + 1
        arr[dx][dy] = 1
        q.append([cnt + 1, dx, dy])

Max = 0
for i in result:
    for d in i :
        if d > Max :
            Max= d
print(Max)