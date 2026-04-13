n,m = map(int,input().split())
nx,ny,nd = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dts = [(-1,0),(0,1),(1,0),(0,-1)]
ans = 0
while 1:
    if arr[nx][ny] == 0 :
        arr[nx][ny] = -1
        ans += 1
    cln = 0
    for i,j in dts :
        dx = nx + i
        dy = ny + j
        if dx <0 or dy < 0 or dx >n-1 or dy > m-1:continue
        if arr[dx][dy] == 0 :
            cln = 1
            break
    if cln == 1 :
        for i in range(1,5) :
            nxtd = dts[(nd - i) % 4]
            dx = nx + nxtd[0]
            dy = ny + nxtd[1]
            if dx <0 or dy < 0 or dx >n-1 or dy >m-1 : continue
            if arr[dx][dy] == 0 :
                nx = dx
                ny = dy
                nd = (nd - i) % 4
                break
    else:
        dx = nx - dts[nd][0]
        dy = ny - dts[nd][1]
        if arr[dx][dy] == 1 :
            break
        else:
            nx,ny = dx,dy





print(ans)