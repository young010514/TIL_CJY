arr=[
    list(map(int,input().split())),
    list(map(int,input().split())),
]
arr_1 = []
for i in arr:
    arr_1.extend(i)
arr_1.sort()
result = [arr_1[:3], arr_1[3:]]
for inner in result:
    [print(x, end=' ') for x in inner]
    print()