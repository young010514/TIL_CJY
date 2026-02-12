# BFS 로 최소 경로 찾기

from collections import deque
from copy import deepcopy
name = "ABCD"
arr = [
    [0,1,1,0],
    [0,0,1,1],
    [0,1,0,1],
    [0,0,0,0],
]
cnt=0
def bfs(start):
    global cnt
    q =deque()
    used = [0] * 4
    used[start] =1
    q.append((start,used))

    while q :
        now = q.popleft()
        if now[0] == 3 : # D 에 도착
            cnt += 1

        for i in range(4):
            if arr[now[0]][i] == 1 and now[1][i] == 0:
                temp = deepcopy(now[1])
                temp[i] = 1
                q.append((i,temp))
bfs(0)
print(cnt)


# BFS
# Flood Fill
from collections import deque
# n = int(input())
# arr = [[0] * n for _ in range(n)]   # n x n 사이즈 배열
# x,y = map(int,input().split())      # 시작 좌표 입력
#
# arr[x][y] = 1 # 시작점 시작일 넣기
# q=deque()
# q.append([y,x,1])
# directx = [0,0,-1,1]
# directy = [-1,1,0,0]
# while q:
#     nowx, nowy, cnt= q.popleft()
#     for i in range(4):
#         dx = directx[i] + nowx
#         dy = directy[i] + nowy
#         if dy <0 or dx < 0 or dx >=n or dy >= n : continue
#         if arr[dx][dy] != 0 :continue
#         arr[dx][dy] = arr[nowx][nowy] + 1
#         q.append([dx,dy,cnt+1])
#
# for i in arr:
#     print(*i)


# 미로찾기

# 0,0,0,0
# 1,0,1,1
# 1,0,1,0
# 0,0,0,0

# 0,0 에서 출발해서 3,3까지 도착하고자 한다.
# 도착이이 가능한지 불가능 한지 출력해 주세요

