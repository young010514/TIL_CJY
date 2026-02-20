n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
st,ed = map(int,input().split())
Max,Min = 0,2e6
def dfs(now, path):
    global Max,Min
    if now == ed :
        Max = max(Max,path)
        Min = min(Min,path)
        return
    for i in range(n):
        if arr[now][i] == 0:continue
        if used[i]==0 :
            used[i] = 1
            dfs(i,path+arr[now][i])
            used[i] = 0

used = [0] * n
used[st] =1
dfs(st,0)
print(Min)
print(Max)
