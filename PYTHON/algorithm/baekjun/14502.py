from copy import deepcopy
from collections import deque
n,m= map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
starts =[]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2: starts.append((i, j))


def spread(lst1):
    dts = [(0,1),(0,-1),(1,0),(-1,0)]
    lst = [row[::] for row in lst1]
    q = deque(starts)

    while q :
        nx,ny = q.popleft()
        for i,j in dts:
            dx = nx+i
            dy = ny+j
            if dx <0 or dy <0 or dx >n-1 or dy >m-1 :continue
            if lst[dx][dy] != 0 : continue
            lst[dx][dy] = 2
            q.append((dx,dy))

    return sum(row.count(0) for row in lst)

result = 0
def dfs(start, level):
    global result
    if level == 3:
        cnt = spread(arr)
        if result < cnt : result = cnt
        return
    for x in range(start+1,n*m):
        i = x //m
        j = x % m
        if arr[i][j] != 0 : continue
        arr[i][j] = 1
        dfs(x,level+1)
        arr[i][j] = 0
dfs(-1,0)
print(result)

