# import sys
# sys.stdin = open("input/input_fire.txt","r")

from collections import deque
n = int(input())
arr = [list(input()) for _ in range(n)]
st = tuple(map(int,input().split()))
fight = [] # 소화전 저장
for i in range(n):
    for j in range(n):
        if arr[i][j] == "A":
            fight.append((i,j))
        elif arr[i][j] == "$":
            fire = (i,j)
dts = [(0,1),(0,-1),(1,0),(-1,0)]
def main(x,y):
    cnt = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((x,y,0))
    cnt[x][y] = 0
    while q:
        nx,ny,now = q.popleft()
        for i,j in dts:
            dx = nx + i
            dy= ny + j
            if dx <0 or dy <0 or dx >n-1 or dy> n-1 :continue  # 배열 범위 벗어난 경우
            if arr[dx][dy] == "#" : continue   # 벽이면
            if arr[dx][dy] == "$" : continue # 불이어도 지나쳐야함
            if cnt[dx][dy] != -1 : continue   # 이미 지나온 경로의 경우
            cnt[dx][dy] = now+1
            q.append((dx,dy,now+1))
    result = []
    for i,j in fight:
        result.append(cnt[i][j])
    return result
arr1 = main(*st)
arr2 = main(*fire)
ans = [arr1[i] + arr2[i] for i in range(len(fight))]
print(min(ans))