n = int(input())
arr = [list(map(int,list(input()))) for _ in range(n)]
result = []
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
from collections import deque
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            q= deque()
            arr[i][j] = 0
            cnt = 0
            q.append((i,j))
            while q:
                nx,ny= q.popleft()
                cnt +=1
                for x,y in dirs:
                    dx= nx+x
                    dy= ny+y
                    if 0<= dx < n and 0<= dy <n:
                        if arr[dx][dy] ==1:
                            arr[dx][dy] = 0
                            q.append((dx,dy))
            result.append(cnt)
print(len(result))
result.sort()
for i in result:
    print(i)
