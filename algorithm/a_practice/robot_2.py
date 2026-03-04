import sys
sys.stdin = open("input_robot.txt","r")

from collections import deque
directions = [(0,1),(0,-1),(1,0),(-1,0)]


from copy import deepcopy
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr= [list(map(int,input().split())) for _ in range(n)]
    used = [[0] * n for _ in range(n)]
    result = 3e5
    q = deque()
    used[0][0] = 1
    q.append((0,0,0,[(0,0)]))
    while q :
        nx,ny,ns,path = q.popleft()
        if nx == n-1 and ny == n-1 and result > ns:
            result = ns
        for i,j in directions:
            dx = nx + i
            dy = ny + j
            if dx <0 or dy <0 or dx >n-1 or dy>n-1:continue
            if (dx,dy) in path: continue

            if arr[dx][dy] == arr[nx][ny] : gap = 1
            elif arr[dx][dy] > arr[nx][ny] : gap = 2*(arr[dx][dy]-arr[nx][ny])
            else: gap = 0
            q.append((dx,dy,ns+gap, path + [(dx,dy)]))
    print(result)