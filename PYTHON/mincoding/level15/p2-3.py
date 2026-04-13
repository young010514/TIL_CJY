arr=[]
for i in range(3):
    arr.append([])
    for j in range(4):
        arr[i].append(12 - (j + i*4))
num = int(input())
for i in range(4):
    arr[num-1][i] = 7
for inner in arr:
    for x in inner:
        print(x,end=' ')
    print()