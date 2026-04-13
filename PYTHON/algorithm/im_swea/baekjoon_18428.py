n = int(input())
arr= [input().split() for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == "T":



if cnt > 3: print("NO")
else:print("YES")