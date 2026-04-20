arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
num = int(input())
for a in range(5):
    for b in range(5):
        if a % 4 == 0 or b % 4 ==0:
            arr[a][b] = num
for inner in arr:
    for i in inner:
        if i :print(i, end='')
        else:print("_", end='')
    print()

