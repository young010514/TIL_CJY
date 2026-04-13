from collections import deque
def bfs(x,y):
    global  result,arr
    dts = [(0,1),(0,-1),(1,0),(-1,0)]
    q = deque()
    arr[x][y] = 0
    q.append((x,y))
    cnt = 1
    while q:
        nx,ny = q.popleft()
        for i,j in dts:
            dx = nx + i
            dy = ny + j
            if dx <0 or dy <0 or dx > n-1 or dy >n-1 :continue
            if arr[dx][dy] == 0:continue
            arr[dx][dy] = 0
            q.append((dx,dy))
            cnt += 1
    result.append(cnt)

n = int(input())
arr = [list(map(int,list(input()))) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:continue
        bfs(i,j)
result.sort()
print(len(result))
for i in result:print(i)
