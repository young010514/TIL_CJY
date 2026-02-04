import sys
sys.stdin = open("input_space.txt","r")

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    directions = []
    for a in range(-1,2):
        for b in range(-1,2):
            directions.append((a,b))
    result = 0
    for i in range(0,N):
        for j in range(0,M):
            cnt = 0
            for dx, dy in directions:
                if 0 <= i + dx < N and 0<= j + dy <M:
                    if arr[i+dx][j+dy] <arr[i][j]: cnt +=1
            if cnt >=4 : result += 1

    print(f"#{t+1} {result}")