from collections import deque
e_dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
a_dirs = e_dirs[:4] + [(0,0)]   # 상하좌우 + 제자리 가능


n = int(input())
arr =[list(input()) for _ in range(n)]
a,b,c,d = map(int,input().split())


q1, q2 = deque(), deque()
used = [[0] * n for _ in range(n)]
used[a][b], used[c][d] = 1,1

q1.append((a,b,0))  # 엘사 x,y, route_sum
q2.append((c,d,0))  # 안나 x,y, route_sum
result = 0
while q1 and q2 :
    nx1, ny1, r1 = q1.popleft()
    nx2, ny2, r2 = q2.popleft()
    if nx1 == nx2 and ny1 == ny2 and r1 == r2 :
        result= r1
        break
    for i,j in a_dirs:
        if i == 0 and j == 0 :q2.append((nx2,ny2, r2+1))
        dx2 = nx2 + i
        dy2 = ny2 + j
        if 0<= dx2< n and 0<= dy2 <n :
            if arr[dx2][dy2] =="_" and used[dx2][dy2] == 0:
                used[dx2][dy2] = 1
                q2.append((dx2,dy2,r2+1))
    if abs(nx1-nx2) + abs(ny1-ny2) <= 4:
        dirs = e_dirs[:4]
    else: dirx = e_dirs
    for i,j in dirs:
        dx = nx1 + i
        dy = ny1+j
        if 0<= dx <n and 0<= dy <n  :
            if arr[dx][dy] == "_" and used[dx][dy] ==0:
                used[dx][dy] = 1
                q1.append((dx,dy,r1+1))

print(result)
