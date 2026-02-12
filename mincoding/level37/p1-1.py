n = int(input())
arr = [[0] * n for _ in range(n)]
a1,b1, a2,b2 = map(int,input().split())
for i in range(n):
    for j in range(n):
        arr[i][j] = abs(a1-i) + abs(b1-j) +1
for i in range(n):
    for j in range(n):
        if arr[i][j] > abs(a2-i) + abs(b2-j)+1:
            arr[i][j] = abs(a2-i) + abs(b2-j)+1
for i in range(n):
    for j in range(n):
        print(arr[i][j],end='')
    print()





