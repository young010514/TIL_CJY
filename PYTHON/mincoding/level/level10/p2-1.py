arr = []
for a in range(4):
    arr.append([])
    for b in range(4):
        arr[a].append(2 * (a+1) + b * 8)
for inner in arr:
    [print(x, end=' ') for x in inner]
    print()