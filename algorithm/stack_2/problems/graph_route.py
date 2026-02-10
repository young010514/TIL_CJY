import  sys
sys.stdin = open("input_route.txt", "r")

T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    arr = [[0] * v for _ in range(v)]
    visited = [0] * v

    for _ in range(e):
        x,y = map(int,input().split())
        arr[x-1][y-1] = 1

    s,g = map(int,input().split())
    result = 0

    def route(node):
        global  result
        if node == g-1:
            result = 1
            return
        if sum(arr[node]) == 0:
            return
        for i in range(v):
            if arr[node][i] == 1 and visited[i] == 0:
                visited[i] = 1
                route(i)

    route(s-1)
    print(f"#{tc} {result}")