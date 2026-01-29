arr = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for i in range(6):
    for j in range(3):
        arr[-i-1][-j-1] = chr(ord('A') + i  + j*6)
# print(arr)
a, b = map(int,input().split())
print(arr[a][b])