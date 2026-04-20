n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
for j in range(len(arr[0])):
    data = 0
    for i in range(n):
        data += arr[i][j]
    if data == 0 : boss = j

under = []
for i in range(n) :
    if arr[0][i] == 1: under.append(i)
print(f"boss:{boss}")
print("under:",end='')
print(*under)