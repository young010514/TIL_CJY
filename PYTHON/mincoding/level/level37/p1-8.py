from collections import deque

directions = [(0,1),(0,-1),(1,0),(-1,0)]
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
brk = True
cnt = 0
while brk:
    brk = False
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 :
                brk = True
                stx,sty = i,j
                break
    if brk == False : break
    cnt +=1
    q = deque()
    q.append((stx,sty))
    while q:
        nowx, nowy = q.popleft()
        for i,j in directions:
            dx = nowx+i
            dy = nowy+j
            if dx < 0 or dy < 0 or dx >=n or dy >=m : continue
            if arr[dx][dy] == 0 :continue
            else:
                arr[dx][dy] = 0
                q.append([dx,dy])
print(cnt)