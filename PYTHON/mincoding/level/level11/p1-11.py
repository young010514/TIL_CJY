arr = [[1,3,6,2],[4,2,4,5],[6,3,7,3],[1,5,4,6]]
n = int(input())
result =[]
for inner in arr:
    for x in inner:
        if x > n : result.append(x)

for x in result :
    print(x, end=' ')
    