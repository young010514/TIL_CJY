arr = []
for i in range(7):
    arr.append([])
    for j in range(4):
        arr[i].append(1 + i*4 + j)

arr1 = list(map(int,input().split()))
for i in arr1:
    arr[i] = [0,0,0,0]
for inner in arr:
    [print(x,end=' ') for x in inner]
    print()