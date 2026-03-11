import sys
sys.stdin = open("input_mincost.txt","r")

# 힙정렬로 풀어야하는거같음

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    used = [[0] * n for _ in range(n)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    result = 5e10

    def dfs(x,y,Sum):
        global result

        # 이미 합이 더 크다면 그냥 끄기
        if Sum >result: return
        if x == n-1 and y == n-1:
            if result > Sum :
                result = Sum
            return
        for i,j in directions:
            dx = x + i
            dy = y + j
            if dx <0 or dy <0 or dx > n-1 or dy > n-1 : continue
            if used[dx][dy] == 1: continue
            used[dx][dy] =1
            if arr[dx][dy] <= arr[x][y] : dfs(dx,dy,Sum+1)
            else: dfs(dx,dy, Sum + 1 + (arr[dx][dy] - arr[x][y]))
            used[dx][dy] =0
    used[0][0]= 1
    dfs(0,0,0)
    print(f"#{tc} {result}")