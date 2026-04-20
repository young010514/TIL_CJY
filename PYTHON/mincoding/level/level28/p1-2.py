lst = ['Bob','Chloe','Amy','Edger','Diane']
arr = [
    [0,0,1,0,0],
    [1,0,0,0,0],
    [0,0,0,1,0],
    [0,0,0,0,0],
    [1,0,0,0,0],
]
result = []
for j in range(len(arr[0])):
    data = 0
    for i in range(len(arr)):
        data += arr[i][j]
    result.append(data)
print(lst[result.index(max(result))])