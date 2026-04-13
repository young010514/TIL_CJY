from collections import deque

arr = [list(map(int,input().split())) for _ in range(4)]
used = [[0]*6 for _ in range(4)]
directions = [(1,0),(-1,0),(0,1),(0,-1)]
ans = 0
q = deque()
q.append([0,0])
while q:
    x,y = q.popleft()

    for i,j in directions:
        dx = x+i
        dy = y+j
        if dx < 0 or dy< 0 or dx >= 4 or dy >= 6:continue
        if arr[dx][dy] ==1 :continue
        if used[dx][dy] == 0 :
            if arr[dx][dy] == 2: ans += 1
            used[dx][dy] = 1
            q.append([dx,dy])
print(ans)
