arr = [
    [0,0,0,0,1,0],
    [1,0,1,0,0,1],
    [1,0,0,1,0,0],
    [1,1,0,0,0,0],
    [0,1,0,1,0,1],
    [0,0,1,1,0,0],
]
n = int(input())
path =[0]*len(arr)

def abc(idx):
    if sum(path) == len(arr):
        return
    for i in range(len(arr[0])) :
        if path[i] == 0 : print(i)
    for i in range(len(arr[0])):
        if path[i] == 0:
            path[i] =1
            abc(i)
print(n)
path[n]=1
abc(n)