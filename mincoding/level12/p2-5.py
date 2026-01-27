arr1 = [[4,5,4,5,4],[8,9,8,9,8],[1,2,1,2,1],[4,5,4,5,4],[6,7,6,7,6]]

for i in range(5):
    a, b= map(int,input().split())
    arr1[a][b] += 1
    if arr1[a][b] == 10 : arr1[a][b] = 0

for inner in arr1:
    [print(x,end='') for x in inner]
    print()