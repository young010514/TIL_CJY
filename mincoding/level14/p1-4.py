arr1 = input().split()
arr = []
for i in range(5):
    arr.append([])
    for x in arr1[i:]:
        arr[i].append(x)

for inner in arr:
    for x in inner:
        print(x, end= ' ')
    print()