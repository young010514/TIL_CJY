from collections import deque

n,m = map(int,input().split())
arr= [input().split() for _ in range(n)]
# 우선 치즈로
# 다음엔 도시한테로 가야하는데,
# 이걸 for _ in range(2)로 구현해보기

directions = [(1,0),(-1,0),(0,1),(0,-1)]
s,d,c = 0,0,0

for i in range(n):
    if "S" in arr[i]: s = (i, arr[i].index("S"))
    if "C" in arr[i]: c = (i, arr[i].index("C"))
    if "D" in arr[i]: d = (i, arr[i].index("D"))
    if s and d and c : break
Sum = 0
# 우선 도착 치즈

def bfs(s,e):
    sx,sy = s[0],s[1]
    ex, ey = e[0],e[1]
    used = [[0] * m for _ in range(n)]

    q = deque()
    q.append((sx,sy,0)) # x,y,cnt
    used[sx][sy] = 1
    while q:
        nx,ny,cnt = q.popleft()
        if nx == ex and ny == ey :
            return cnt
        for i,j in directions:
            dx = nx + i
            dy = ny + j
            if 0<= dx <n and 0<= dy <m :
                if arr[dx][dy] != "x" and used[dx][dy] == 0:
                    used[dx][dy] = 1
                    q.append((dx,dy,cnt+1))

result = bfs(s,c) + bfs(c,d)
print(result)