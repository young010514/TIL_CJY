# import sys
# sys.stdin = open("input_fire.txt","r")


from collections import deque
n = int(input())
arr = [list(input()) for _ in range(n)]

x,y = map(int,input().split())

directions = [(0,1),(0,-1),(1,0),(-1,0)]
# 불 위치 찾기
for i in range(n):
    if "$" in arr[i] :
        fx, fy = i, arr[i].index("$")
def to_A(stx, sty, edx, edy):
    used = [[0] * n for _ in range(n)]
    q = deque()
    q.append((stx, sty, 0)) # x, y ,cnt
    used[stx][sty] = 1
    cnt = -1
    while q:
        nx,ny,cnt = q.popleft()
        if nx == edx and ny == edy:
            return cnt
        for i,j in directions:
            dx = nx + i
            dy = ny + j
            if 0<= dx < n and 0<= dy < n:
                if (arr[dx][dy] == "_" or arr[dx][dy] == "A") and used[dx][dy] == 0:
                    used[dx][dy] = 1
                    q.append([dx,dy, cnt +1])

def to_fire(stx,sty):
    used = [[0] * n for _ in range(n)]
    q = deque()
    q.append([stx, sty, 0])  # x, y ,cnt
    cnt = -1
    used[stx][sty] = 1
    while q:
        nx, ny, cnt = q.popleft()
        if nx == fx and ny == fy :
            return cnt
        for i, j in directions:
            dx = nx + i
            dy = ny + j
            if 0 <= dx < n and 0 <= dy < n:
                if arr[dx][dy] != "#" and used[dx][dy] == 0:
                    used[dx][dy] = 1
                    q.append([dx, dy, cnt + 1])
result = 5e10
for i in range(n):
    for j in range(n):
        if arr[i][j] == "A" :
            data = to_A(x,y,i,j) + to_fire(i,j)
            if data < result : result = data
print(result)