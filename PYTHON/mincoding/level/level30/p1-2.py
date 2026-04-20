arr=[
    [0,0,1,0,2,0],
    [5,0,3,0,0,0],
    [0,0,0,0,0,7],
    [2,0,0,0,8,0],
    [0,0,9,0,0,0],
    [4,0,0,7,0,0],
]
n = int(input())
def abc(idx,path,data):
    if idx in path[:-1]:
        return
    print(f"{idx} {data}")
    for i in range(len(arr[0])):
        if arr[idx][i] != 0 and i not in path:

            data += arr[idx][i]
            path.append(i)
            abc(i,path,data)


abc(n,[n],0)