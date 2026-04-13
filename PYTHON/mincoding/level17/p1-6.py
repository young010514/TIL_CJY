arr1 = [
    [0,0,0,1],
    [1,1,0,1],
    [1,0,0,1],
    [1,1,1,1],
]
arr2 = [
    [1,1,1,1],
    [1,0,1,1],
    [1,0,0,0],
    [1,0,0,0],
]
result = []
for i in range(4):
    result.append([])
    for j in range(4):
        result[i].append(arr1[i][j] + arr2[i][j])

for i in range(4):
    for j in range(4):
        if not result[i][j] :print(f"({i},{j})")
