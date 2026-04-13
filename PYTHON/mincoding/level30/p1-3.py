arr = [
    [0,1,0,0,1,0],
    [0,0,1,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]
n = int(input())
def abc(idx):
    if sum(arr[idx]) ==0:
        return
    for i in range(len(arr[0])):
        if arr[idx][i] ==1:
            print(i,end=' ')
    for i in range(len(arr[0])):
        if arr[idx][i] ==1:
            abc(i)
print(n,end=' ')
abc(n)