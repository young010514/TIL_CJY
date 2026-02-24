arr = [list(map(int,input().split())) for _ in range(4)]

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
used = [[0] *9 for _ in range(4)]
def bee(nx,ny):
    global Sum,cnt
    for i,j in dirs:
        dx = nx + i
        dy = ny+j
        if 0<= dx <4 and 0<= dy < 9:
            if arr[dx][dy] != arr[nx][ny]:continue
            if used[dx][dy] ==0:
                used[dx][dy] =1
                Sum += arr[dx][dy]
                cnt +=1
                bee(dx,dy)
result = 0
for i in range(4):
    for j in range(9):
       if used[i][j] == 0:
           cnt = 1
           Sum = arr[i][j]
           used[i][j] = 1
           bee(i,j)
           if cnt > result :
               result = cnt
               result_sum = Sum
print(result_sum)