directions = [(0,1),(0,-1),(1,0),(-1,0)]
arr = [list(map(int,input().split())) for _ in range(4)]
used = [[0] * 4 for _ in range(4)]

area =1




from collections import deque
q = deque()
used[0][0] = 1
q.append([0,0])
while q:
    x,y = q.popleft()
    for i,j in directions:
        dx = x+i
        dy = y+j
        if dx <0 or dy <0 or dx >=4 or dy >= 4:continue
        if arr[dx][dy] == 0:continue
        if used[dx][dy] == 0:
            area +=1
            used[dx][dy] = 1
            q.append([dx,dy])
print(area)