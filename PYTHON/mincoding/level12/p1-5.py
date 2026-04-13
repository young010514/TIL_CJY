n = int(input())
arr = []
for i in range(3):
    arr.append([])
    for j in range(4):
        if i + j <= 1 : arr[i].append(0)
        else:
            arr[i].append(n)
            n += 1
for inner in arr:
    for x in inner:
        if not x :print(' ',end='')
        else:
            print(x, end='')
    print()