lst = [10,40,60]
Min = 21e5
n = int(input())
def dfs(data):
    global Min
    if sum(data) >= n :
        if sum(data) == n and len(data) < Min :
            Min = len(data)
        return
    for i in lst:
        data.append(i)
        dfs(data)
        data.pop()
dfs([])
print(Min)