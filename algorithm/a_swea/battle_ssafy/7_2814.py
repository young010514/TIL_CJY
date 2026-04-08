import sys
sys.stdin = open("input_7.txt","r")

def dfs(now, level):
    global result
    if level > result :
        result = level
    for i in lines[now]:
        if visited[i] == 1 : continue
        visited[i] = 1
        dfs(i,level +1)
        visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    lines = [[] for _ in range(1+n)]
    lines[0] = list(range(1,n+1))
    visited = [0] * (n+1)
    visited[0] = 1
    for i in range(m):
        x,y = map(int,input().split())
        lines[x].append(y)
        lines[y].append(x)
    result =0
    dfs(0,0)
    print(f"#{tc} {result}")