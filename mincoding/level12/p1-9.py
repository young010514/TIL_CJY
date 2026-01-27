arr1 = [[0,0,0],[0,0,0],[0,0,0]]

n = input()
num = 6
if n.isnumeric() and 0 <= int(n) <= 9:
    for x in range(3):
        for y in range(3-x):
            arr1[x][y+x] = num
            num -= 1
elif n.isupper():
    for x in range(3):
        for y in range(x, -1, -1):
            arr1[x][y] = num
            num -= 1
for inner in arr1:
    for i in inner:
        if i :print(i, end='')    
        else:print(' ', end='')
    print()

