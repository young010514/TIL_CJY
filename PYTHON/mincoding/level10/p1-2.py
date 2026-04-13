arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
n = int(input())
if n % 2 ==0 : 
    for i in range(4):
        arr[i][i] = i+1
else:
    for i in range(4):
        arr[i][3-i] = i+1
for inner in arr:
    for data in inner:
        print(data, end=' ')
    print()