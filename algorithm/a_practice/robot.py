import sys
sys.stdin = open("input_robot.txt","r")

directions = [(0,1),(0,-1),(1,0),(-1,0)]



T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr= [list(map(int,input().split())) for _ in range(n)]
    used = [[0]*n for _ in range(n)]
    ret = 10e6
    def dfs(x,y,ns):
        global ret
        if x == n-1 and y==n-1 and ret > ns :
            ret = ns
        for i,j in directions:
            dx = x+i
            dy = y+j
            if dx <0 or dy< 0 or dx >n-1 or dy>n-1 :continue
            if used[dx][dy] ==1 : continue

            used[dx][dy] =1
            if arr[x][y] == arr[dx][dy] : gap = 1
            elif arr[dx][dy] > arr[x][y]:
                gap = 2*(arr[dx][dy] - arr[x][y])
            else:gap = 0
            dfs(dx,dy,ns + gap)
            used[dx][dy] =0
    used[0][0] = 1
    dfs(0,0,0)

    print(f"#{tc} {ret}")
