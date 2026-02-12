from collections import deque
from copy import deepcopy
stx, sty = map(int,input().split())
edx, edy = map(int,input().split())


arr = [[0,0,0,0],[1,1,0,1],[0,0,0,0],[1,0,1,0]]
used = [[0]*4 for _ in range(4)]
used[stx][sty] = 1
q= deque()
q.append((stx,sty, used, 0)) # x,y,경로길이

directions = [(1,0),(-1,0),(0,1),(0,-1)]
result  = 1000
while q:
    x,y,used,ans = q.popleft()

    if x == edx and y == edy :
        if result > ans : result = ans
        break

    temp = deepcopy(used)

    for i,j in directions:
        dx = x+i
        dy = y+j

        if dx < 0 or dy < 0 or dx >= 4 or dy >= 4:continue
        if arr[dx][dy] == 0 and temp[dx][dy] == 0 :
            temp[dx][dy] = 1
            q.append((dx,dy,temp,ans+1))

print(f'{result}회')



