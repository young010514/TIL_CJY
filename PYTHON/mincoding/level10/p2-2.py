arr= []
for a in range(5):
    arr.append([])
    for b in range(5):
        arr[a].append(21 + a - 5*b)
n = int(input())
for a in range(5):
    arr[n][a] = n
for inner in arr:
    [print(x, end=' ') for x in inner]
    print()