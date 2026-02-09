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
    for i in range(6) :
        if path[i] == 0 and arr[idx][i]==1: 
            print(i)
    for i in range(6):
        if path[i] == 0  and arr[idx][i]==1:
            path[i] =1
            abc(i)
print(n)
path[n]=1
abc(n)