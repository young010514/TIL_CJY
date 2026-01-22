arr = []
for i in range(6):
    arr.append([])
    for j in range(3):
        arr[i].append(10+i + j*6)
a, b =map(int,input().split())
for i in range(a, b+1):
    arr[i] = [7,7,7]
for inner in arr:
    [print(x,end=' ') for x in inner]
    print()