import sys
sys.stdin = open("input_mincost.txt","r")

def bfs(x, Sum):
    global y_axis, n, result
    if Sum > result : return
    if x == n :
        if result > Sum:
            result = Sum
        return
    for i in range(n):
        if y_axis[i] == 1: continue
        y_axis[i] = 1
        bfs(x+1, Sum + arr[x][i])
        y_axis[i] = 0

T =int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    y_axis = [0] * n
    result = 2e7

    bfs(0,0)
    print(f"#{tc} {result}")