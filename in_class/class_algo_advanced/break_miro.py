from collections import deque

arr = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0]
]

visited = [[[0] *5 for _ in range(5)] for _ in range(3)]
visited[0][0][0] = 1
dts = [(0,1),(0,-1),(1,0),(-1,0)]
q = deque()
q.append((0,0,0,0))  # x,y, cnt, break
result = -1
while q:
    nx,ny,cnt,breaks = q.popleft()
    if nx==4 and ny == 4 :
        result = cnt
        break
    for i,j in dts:
        dx = nx +i
        dy = ny +j
        if dx <0 or dx >4 or dy<0 or dy>4 : continue
        if visited[breaks][dx][dy] == 1 :continue
        if arr[dx][dy] ==1:
            if breaks + 1 > 2 or visited[breaks][dx][dy] == 1 : continue
            visited[breaks+1][dx][dy] =1
            q.append((dx,dy,cnt+1,breaks+1))
        else:
            visited[breaks][dx][dy] =1
            q.append((dx,dy,cnt+1, breaks))
print(result)