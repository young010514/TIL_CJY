dts = [(0,1),(0,-1),(1,0),(-1,0)]
T = int(input())
def dfs(level,x,y, st):
    global result
    if level == 7:
        if st in result : return
        result.append(st)
        return
    for i,j in dts:
        dx = x+i
        dy = y+j
        if dx <0 or dx >3 or dy <0 or dy>3 : continue
        dfs(level +1, dx,dy, st + arr[dx][dy])

for tc in range(1,T+1):
    arr = [input().split() for _ in range(4)]
    result = []
    for i in range(4):
        for j in range(4):
            dfs(0,i,j, "")
    print(f"#{tc} {len(result)}")