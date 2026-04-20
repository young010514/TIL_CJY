import copy

# 지금 보는 방향에서 오앞왼뒤 이동했을때의 y offset 
ydir = [
    # 오앞왼뒤
    (1,0,-1,0), # 오 
    (0,-1,0,1), # 앞 
    (-1,0,1,0), # 왼 
    (0,1,0,-1)  # 뒤 
]

# 지금 보는 방향에서 오앞왼뒤 이동했을때의 x offset
xdir = [
    # 오앞왼뒤
    (0,1,0,-1), # 오
    (1,0,-1,0), # 앞
    (0,-1,0,1), # 왼
    (-1,0,1,0)  # 뒤
]

# 지금 보는 방향에서 오앞왼뒤 이동하고 나서 보는 방향
face  = [
    # 오앞왼뒤
    (3, 0, 1, 2), #오 
    (0, 1, 2, 3), #앞
    (1, 2, 3, 0), #왼
    (2, 3, 0, 1)  #뒤
]

def sim(y, x, dir) :

    days = M
    cnt = 0
    seedcnt = [[0 for _ in range(N)] for _ in range(N)]
    seeds = []
    
    while days > 0 :
        harvested = False
        days -= 1

        size = len(seeds) 
        for _ in range(size) :
            now = seeds.pop(0)
            now[2] += 1
            if now[2] == (3 + seedcnt[now[0]][now[1]]) :
                mapcopy[now[0]][now[1]] = 3
            else :
                seeds.append(now)

        if mapcopy[y][x] == 3 :
            cnt += 1
            mapcopy[y][x] = 0
            harvested = True 

        nextdir = -1
        for i in range(4) :
            ny = y + ydir[dir][i]
            nx = x + xdir[dir][i]
            if mapcopy[ny][nx] == 1 or mapcopy[ny][nx] == 2 :
                continue
            nextdir = i
            break 

        if nextdir == -1 :
            continue 

        if mapcopy[y][x] == 0 and harvested == False: 
            mapcopy[y][x] = 2
            seedcnt[y][x] += 1
            seeds.append([y, x, -1])

        y = y + ydir[dir][nextdir]
        x = x + xdir[dir][nextdir]
        dir = face[dir][nextdir]

    return cnt
        

T = int(input())
for tc in range(1, T+1) :

    # input 
    N, M = list(map(int, input().split()))
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # solve - 모든 위치에서 모든 방향으로 두기
    for i in range(N) :
        for j in range(N) : 
            # 산이라면 pass
            if MAP[i][j] == 1 : 
                continue 
            for d in range(4) : 
                mapcopy = copy.deepcopy(MAP)
                temp = sim(i, j, d) 
                ans = max(temp, ans)

    # output
    print(f"#{tc} {ans}")
