lst = list('ABCDEFGH')
arr=[
    [0,1,1,0,0,0,0,1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
n = input()
idx = lst.index(n)
parent = ''
for i in range(len(arr)):
    if arr[i][idx] == 1:
        parent = i
result =[]
if parent != "":
    for i in range(len(arr[0])):
        if arr[parent][i] == 1:
            if lst[i] != n : result.append(lst[i])
if result : print(*result)
else:print("없음")