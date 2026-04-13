n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n-1)]
used = [0] * (n+1)
result = -1
def dfs(node):
    for a,b in arr:
        if b != node : continue
        if used[a] == 1: continue
        used[a] =1
        dfs(a)

for i in range(1,n+1):
    used[i] = 1
    dfs(i)
    if sum(used) == n : 
        result = i
        break
    used = [0] *(n+1)
print(result)