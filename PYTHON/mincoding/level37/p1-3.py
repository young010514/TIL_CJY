directions = [
    (-1,0),
    (1,0),
    (0,1),
    (0,-1),
    (1,1),
    (1,-1),
    (-1,1),
    (-1,-1),
]
from collections import deque
arr = [list(map(int,input().split())) for _ in range(4)]
q = deque()
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1 :
            q.append([i,j,0])
while q :
    x,y,cnt = q.popleft()

    for i,j in directions:
        dx = x + i
        dy = y + j
        if dx <0 or dy < 0 or dx >= 4 or dy >=5 :continue
        if arr[dx][dy] == 1: continue
        arr[dx][dy] =1
        q.append([dx,dy, cnt+1])
print(cnt)