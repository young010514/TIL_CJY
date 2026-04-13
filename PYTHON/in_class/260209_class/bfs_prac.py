n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
directions = [(0,1),(0,-1),(1,0),(-1,0)]
result = 0

def dfs(x,y,level,Sum):
    global  result
    if level == 4 :
        if result < Sum : result = Sum
        return
    for i,j in directions:
        dx = x + i
        dy = y + j
        if dx <0 or dy <0 or dx > n-1 or dy >n-1:continue
        if used[dx][dy] == 1:continue
        used[dx][dy] =1
        dfs(dx,dy,level+1, Sum + arr[dx][dy])
        dfs(x,y,level+1, Sum + arr[dx][dy])
        used[dx][dy] = 0
for i in range(n):
    for j in range(m):
        used = [[0]*m for _ in range(n)]
        used[i][j] = 1
        dfs(i,j,1,arr[i][j])
print(result)