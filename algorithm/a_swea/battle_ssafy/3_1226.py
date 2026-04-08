import sys
sys.stdin = open("input_3.txt","r")

from collections import deque

def find(arr):
    for i in range(16):
        for j in range(16):
            if arr[i][j] == "2":
                return i,j
def miro(arr):
    global sx,sy
    dts = [(0,1),(0,-1),(1,0),(-1,0)]
    q = deque()
    q.append((sx,sy))
    while q:
        nx,ny = q.popleft()
        for i,j in dts:
            dx = nx + i
            dy = ny + j
            if dx <0 or dy<0 or dx>15 or dy >15: continue
            if arr[dx][dy] == "1" : continue
            elif arr[dx][dy] == "3":
                return 1

            arr[dx][dy] ="1"
            q.append((dx,dy))
    return 0

for _ in range(10):
    n = int(input())
    arr = [list(input()) for _ in range(16)]
    sx, sy = find(arr)

    result = miro(arr)

    print(f"#{n} {result}")
