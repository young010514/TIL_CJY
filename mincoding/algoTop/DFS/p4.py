arr = [list(input()) for _ in range(3)]
used = [[0]*3 for _ in range(3)]
cnt =0
dirx=[0,0,1,-1]
diry=[1,-1,0,0]
def dfs(x,y,path):  # x,y,string
    global cnt
    if x == 2 and y == 2 :
        if path == path[::-1] :

            cnt +=1
        return
    for i in range(4):
        dx = dirx[i] + x
        dy = diry[i] + y
        if 0 <= dx < 3 and 0<= dy < 3:
            if used[dx][dy] == 0:
                used[dx][dy] = 1
                dfs(dx,dy, path+arr[dx][dy])
                used[dx][dy] = 0
used[0][0]=1
dfs(0,0,arr[0][0])
print(cnt)