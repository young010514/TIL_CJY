import sys
sys.stdin = open("input_2.txt","r")

def find(n,arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "X":
                return i,j
def move(c,command) :
    dts = [(-1,0),(0,1),(1,0),(0,-1)]   # 위, 오른쪽,아래, 왼쪽 (오른쪽 회전)
    nx,ny,nd = sx,sy,0  # 현재 위치와 바라보는 방향 index
    for i in range(int(c)):
        if command[i] == "R":
            nd = (nd + 1) %4
        elif command[i] == "L":
            nd = (nd- 1) %4
        elif command[i] == "A":
            dx = nx + dts[nd][0]
            dy = ny + dts[nd][1]
            if dx <0 or dy< 0 or dx >n-1 or dy>n-1 : continue
            if arr[dx][dy] == "T":continue
            nx, ny = dx, dy
    if arr[nx][ny] == "Y": return 1
    else: return 0


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    sx,sy = find(n,arr)

    q = int(input())
    print(f"#{tc}",end=' ')
    for _ in range(q):
        c, command = input().split()
        result = move(c,command)
        print(result,end=' ')
    print()
