arr = []
for a in range(4):
    arr.append([])
    for b in range(4):
        arr[a].append(a+13 - 4 * b)
for inner in arr:
    [print(x,end=' ') for x in inner]
    print()