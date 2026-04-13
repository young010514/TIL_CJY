arr = []
for x in range(4):
    inner = list(map(int,input().split()))
    arr.append(inner)
for x, inner in enumerate(arr):
    for y, data in enumerate(inner):
        if data ==0 : arr[x][y] = "!"
        elif data% 2 == 0 :arr[x][y] = "#"
        else: arr[x][y] = "@"
for inner in arr:
    [print(x, end='') for x in inner]
    print()