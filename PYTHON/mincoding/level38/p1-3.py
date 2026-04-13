arr = [list(map(int,list(input()))) for _ in range(7)]

def flood(nx, ny):
    now = arr[nx][ny]
    now_d =now + 2
    for i in range(7):
        for j in range(7):
            if i== nx and j == ny : continue
            if arr[i][j] != now: continue
            gap = abs(nx-i) + abs(ny-j)
            arr[i][j] = 0
            if gap < now_d:
                return False
    return True

for i in range(7):
    for j in range(7):
        if arr[i][j] ==1 :
            result1= flood(i,j)
            break

for i in range(7):
    for j in range(7):
        if arr[i][j] ==2 :
            result2= flood(i,j)
            break

if result1 and result2: print("pass")
else: print("fail")

