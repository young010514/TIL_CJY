n = int(input())
arr = []
for a in range(3):
    arr.append([])
    for b in range(4):
        arr[a].append(4*(3-a) - b)
for x in range(3):
    arr[x][n] = 0
for inner in arr:
    [print(x, end= ' ') for x in inner]
    print()