import sys
sys.stdin = open("input_theif.txt","r")

from collections import deque
directions = [(-1,0),(0,1),(1,0),(0,-1)]
structs = [[], directions[:],directions[::2], directions[1::2],directions[:2],directions[1:3],directions[2:4],directions[::3]]

def bfs(x,y):
    global used, ans, l
    q = deque()
    used = [[0] * m for _ in range(n)]
    used[r][c] = 1
    q.append((1,x,y))   # hours, x,y
    while q:
        nh, nx, ny = q.popleft()
        # 이미 최대 시간이라면 굳이 더 추가할 필요없이 continue
        if nh == l : continue
        for i,j in structs[arr[nx][ny]]:
            dx = nx + i
            dy = ny + j
            if dx <0 or dy < 0 or dx > n-1 or dy > m-1 : continue
            if used[dx][dy] ==1 or arr[dx][dy] == 0 : continue
            if (-i,-j) not in structs[arr[dx][dy]] : continue
            used[dx][dy] = 1
            ans += 1
            q.append((nh+1,dx,dy))


T = int(input())
for tc in range(1,T+1):
    n,m,r,c,l= map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = 1
    bfs(r,c)
    print(f"#{tc} {ans}")