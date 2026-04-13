from collections import deque
while 1 :
    l,r,c = map(int,input().split())
    if l==0 and r == 0 and c ==0 :
        break
    arr =[]
    for i in range(l):
        arr.append([])
        for j in range(r):
            lst = input()
            arr[i].append(lst)
            if "S" in lst :
                st = (i,j,lst.index("S"))
        input()
    # print(st)
    used=[[[0] * c for _ in range(r)] for _ in range(l)]
    def escape():
        dts = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
        q =deque([(st[0],st[1],st[2],0)])
        while q:
            nx,ny,nz,nt = q.popleft()
            if arr[nx][ny][nz] == "E":
                return f"Escaped in {nt} minute(s)."
            for i,j,k in dts:
                dx = nx + i
                dy = ny + j
                dz = nz + k
                if dx <0 or dy <0 or dz <0 or dx > l-1 or dy > r-1 or dz >c-1:continue
                if used[dx][dy][dz] == 1: continue
                if arr[dx][dy][dz] == "#" :continue
                used[dx][dy][dz] = 1
                q.append((dx,dy,dz,nt+1))
        return "Trapped!"
    print(escape())

