n = list(input())

def dfs(level,prev,path):
    if level ==3 :
        print(path)
        return
    for i in range(prev,len(n)):
        dfs(level+ 1, i,path + n[i])
dfs(0,0,"")