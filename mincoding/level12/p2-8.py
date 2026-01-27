arr = []
n = int(input())
for x in range(3):
    arr.append([])
    for y in range(3):
        if x + y >1 :
            arr[x].append(n)
            n += 1
        else: arr[x].append(0)
for inner in arr:
    [print(x, end='') for x in inner]
    print()