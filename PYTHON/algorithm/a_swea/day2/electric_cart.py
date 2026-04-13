import sys
sys.stdin = open("input_elecart.txt","r")

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    used = [0] * n
    used[0] = 1
    result = 3e7
    def bfs(level,next,Sum):
        global result
        if Sum > result: return
        if level == n-1 :
            Sum  += arr[next][0]
            if result > Sum :
                result = Sum
            return
        for i in range(n):
            if used[i] == 1 or next == i : continue
            used[i] = 1
            bfs(level+1,i, Sum + arr[next][i])
            used[i] = 0
    bfs(0,0,0)
    print(f"#{tc} {result}")
