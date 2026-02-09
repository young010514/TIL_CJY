lst = list(range(1,7))
arr = [
    [0,0,1,0,1,1],
    [1,0,0,1,0,0],
    [0,0,0,0,1,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [0,0,0,0,0,0],
]

a,b = map(int,input().split())
result = 21e10
def abc(idx, path):
    global result
    if idx == b-1:
        if result > len(path):
            result = len(path)
        return
    for i in range(6):
        if arr[idx][i] == 1:
            if i not in path :
                path.append(i)
                abc(i, path)
                path.pop()

abc(a-1, [])
if result == 21e10 : print(0)
else:print(result)