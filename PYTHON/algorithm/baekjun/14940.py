from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
result = [[-1] * m for _ in range(n)]
def st():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2 :
                st = (i,j)
                return st
st = st()
def main():
    dts = [(0,1),(0,-1),(1,0),(-1,0)]
    q=deque()
    q.append((st[0],st[1], 0))
    while q:
        nx,ny,cost = q.popleft()
        for i,j in dts:
            dx =nx +i
            dy = ny + j
            if dx <0 or dy <0 or dx >n-1 or dy> m-1 :continue
            if arr[dx][dy] == 0 :continue
            if result[dx][dy] != -1:continue
            if dx==st[0] and dy==st[1] : continue
            result[dx][dy] = cost + 1
            q.append((dx,dy, cost+1))
    result[st[0]][st[1]] = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 :
                result[i][j] = 0
            print(result[i][j], end=' ')
        print()

main()
