a, b= input().split()
arr1 = []
for i in range(5):
    
    arr1.append([0,0,0,0,0])
    if i == int(a) - 1:
        for x in range(-1,-6,-1):
            arr1[i][x] = chr(ord(b)-x-1)

for inner in arr1:
    [print(x, end='') for x in inner]
    print()