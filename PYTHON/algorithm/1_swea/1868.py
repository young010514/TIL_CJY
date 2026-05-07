import sys
sys.stdin = open("input/in_1868.txt","r")

from collections import deque
dts = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1),]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()

        for dx,dy in dts:
            nx = x + dx
            ny = y + dy

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue

            if visited[nx][ny]:
                continue

            if board[nx][ny] == '*':
                continue

            visited[nx][ny] = True

            if board[nx][ny] == 0:
                q.append((nx,ny))
def chg(n):
    global Map
    # arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if Map[i][j] =="*" : continue # 지뢰면 pass
            cnt = 0
            for x,y in dts :
                dx = i+x
                dy = j + y
                if dx <0 or dy <0 or dx >n-1 or dy >n-1 :continue
                if Map[dx][dy] == "*" : cnt +=1
            Map[i][j]=cnt

    # 0부터 찾아서 바꾸기
    ans = 0
    for i in range(n):
        for j in range(n):
            if Map[i][j] ==0 :
                q = deque()
                q.append((i,j))
                while q:
                    nx, ny = q.popleft()
                    Map[nx][ny] = "*"
                    for i, j in dts:
                        dx = nx + i
                        dy = ny + j
                        if dx < 0 or dy < 0 or dx > n - 1 or dy > n - 1: continue
                        if Map[dx][dy] == 0:
                            q.append((dx, dy))
                        else:
                            Map[nx][ny] = "*"
                ans += 1

    for i in range(n):
        for j in range(n):
            if Map[i][j] != "*":
                ans +=1
    return ans

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    Map = [list(input()) for _ in range(n)]
    ans =chg(n)
    print(f"#{tc} {ans}")
    # print(Map)
