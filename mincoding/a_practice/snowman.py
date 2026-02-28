n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            snowman =(i,j)
        elif arr[i][j] == 3:
            jew = (i,j)
