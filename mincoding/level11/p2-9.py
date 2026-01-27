arr1 = list(map(int,input().split()))
arr = [arr1[:2:-1],arr1[2::-1]]
arr2 = []
for inner in arr:
    for x in inner:
        arr2.append(x)

arr2[0], arr2[5] = arr2[5], arr2[0]
[print(x, end=' ') for x in arr2]
