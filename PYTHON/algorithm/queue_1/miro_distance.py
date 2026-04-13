import sys
sys.stdin = open("input_miro.txt","r")

from collections import  deque
t =int(input())

for tc in range(1,t+1):
    n = int(input())
    arr =[list(map(int,list(input()))) for _ in range(n)]
    s,e = 0,0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2: s = (i,j)
            if arr[i][j] == 3: e = (i,j)
            if s and e : break

    directions  = [(0,1),(0,-1),(1,0),(-1,0)]
    def bfs(s,e):
        sx,sy = s
        ex,ey = e
        used = [[0] * n for _ in range(n)]
        q = deque()
        used[sx][sy] = 1
        q.append((sx,sy, 0))
        result = 1000
        while q :
            nx,ny, cnt = q.popleft()
            if nx == ex and ny == ey :
                result = min(result,cnt)
                break
            for i,j in directions:
                dx = nx + i
                dy= ny + j
                if 0<= dx <n and 0<= dy <n :
                    if  arr[dx][dy] != 1 and used[dx][dy] == 0:
                        used[dx][dy] = 1
                        q.append((dx,dy,cnt+1))
        if result == 1000: result = 1
        return result-1
    result = bfs(s,e)
    print(f"#{tc} {result}")