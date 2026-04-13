arr= [
    [0,0,1,1,0,1],
    [0,0,0,1,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [1,0,0,0,0,1],
    [0,0,0,0,0,0],
]

n = int(input())
result = []
def abc(idx,path):
    global result
    if sum(arr[idx]) == 0:
        if len(path) > len(result):
            result = path
        return
    for i in range(6):
        if arr[idx][i] == 1:
            if i not in path :
                path.append(i)
                abc(i, path)
                # path.pop()
abc(n,[n])
print(*result)