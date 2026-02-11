Max = -21e10
Min = 21e10
lst = list(map(int,input().split()))
used = [0] * 5

def dfs(level,path):
    global Max, Min
    if level == 5:
        data = (path[0] * path[1]) -( path[2] * path[3] )+ path[4]
        if data > Max : Max = data
        if data < Min : Min = data
        return
    for i in range(5):
        if used[i] ==0:
            used[i] = 1
            path.append(lst[i])
            dfs(level +1, path)
            used[i] = 0
            path.pop()
dfs(0,[])
print(Max)
print(Min)