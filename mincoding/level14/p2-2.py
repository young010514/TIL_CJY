n = int(input())
arr1 = []
for x in range(5):
    arr= list(map(int,input().split()))
    arr1.append(arr)
result = []
if n == 1:
    for x, inner in enumerate(arr1):
        result.append(inner[:x+1])

elif n == 2:
    for x, inner in enumerate(arr1):
        result.append(inner[:5-x])
for inner in result:
    [print(x, end= ' ') for x in inner]
    print()