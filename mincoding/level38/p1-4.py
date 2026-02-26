arr = [list(input()) for _ in range(8)]

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
used = [[0] * 9 for _ in range(8)]

from collections import deque
q= deque()
used[0][8] = 1
q.append((0,8))
arr1 = []
while q:
    nx,ny = q.popleft()
    cnt =0
    for i,j in dirs:
        dx = nx+i
        dy = ny+j
        if dx <0 or dy <0 or dx >7 or dy > 8 :continue
        if used[dx][dy] == 0 and  arr[dx][dy] == "#":
            used[dx][dy] = 1
            q.append((dx,dy))
            cnt += 1
    if cnt ==0:
        arr1.append((nx,ny))

result = 2e10
q=deque()
q.append((7,0))
used[7][0] = 1
while q :
    nx,ny = q.popleft()
    for i,j in arr1:
        data = abs(i-nx) + abs(j-ny)-1
        if result > data:
            result = data

    for i,j in dirs:
        dx = nx+i
        dy = ny+j
        if dx <0 or dy <0 or dx >7 or dy > 8 :continue
        if used[dx][dy] == 0 and  arr[dx][dy] == "#":
            used[dx][dy] = 1
            q.append((dx,dy))
print(result)

