arr = [[3,5,4],[1,1,2],[1,3,9]]
x, y = map(int,input().split())
result = 0
for i in [-1,1]:
    if 0 <= x + i <= 2:
        result += arr[x+i][y]
    if 0 <= y + i <= 2:
        result += arr[x][y+i]

print(result)