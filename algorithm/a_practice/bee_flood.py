import sys
sys.stdin =open("input_bee_1.txt","r")

# BFS 로 도전
from collections import deque

T = int(input())
for tc in range(1,T+1):

    n,m = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(n)]
    # j 가 짝수일 경우
    dir1= [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1)]
    # j 가 홀수일 경우
    dir2 = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1)]

    Max = 0

    # 한 점을 시작으로 이동하는 경우
    def bee(x,y):
        global  Max

        used = [[0] * m for _ in range(n)]
        q = deque()
        used[x][y] = 1
        q.append((x,y, 1, arr[x][y]))  # x, y, cnt, Sum // cnt == 4이면 Sum이랑 Max랑 비교

        while q :
            nowx, nowy, cnt, nowsum= q.popleft()
            if cnt == 4:
                if nowsum > Max : Max = nowsum
                q.clear()
                break

            # 위치에 따라 갈수 있는 범위 다름
            if nowy % 2 == 0 :
                directions = dir1
            else:
                directions = dir2

            for i,j in directions :
                dx = nowx +i
                dy = nowy + j
                if dx <0 or dy < 0 or dx >=n or dy >= m: continue
                if used[dx][dy] == 1: continue
                used[dx][dy] = 1
                q.append((dx,dy, cnt +1, nowsum + arr[dx][dy]))
    for i in range(n):
        for j in range(m):
            bee(i,j)

    print(f"#{tc} {Max}")