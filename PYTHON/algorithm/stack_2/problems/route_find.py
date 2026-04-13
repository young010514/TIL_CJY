import sys
sys.stdin = open("input_find.txt", "r")



for _ in range(10):
    result = 0
    tc, n = map(int,input().split())
    lst = list(map(int,input().split()))
    visited = [0] * 100
    arr = [[0] * 100 for _ in range(100)]
    for i in range(n):
        arr[lst[2*i]][lst[2*i+1]] = 1


    def route(node):
        global result
        if node == 99:
            result = 1
            return
        if sum(arr[node]) == 0:
            return
        for i in range(100):
            if arr[node][i] == 1 and visited[i] == 0 :
                visited[i] = 1
                route(i)
    route(0)
    print(f"#{tc} {result}")