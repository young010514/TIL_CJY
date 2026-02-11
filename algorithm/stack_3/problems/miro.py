import sys
sys.stdin = open("input_miro.txt", "r")

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    result = 0

    # start 찾기
    for i in range(n):
        if arr[i].find("2") != -1:
            start = (i,arr[i].index("2"))

    # 근접 directions
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    def miro(*point):
        x,y = point
        visited[x][y] = 1
        will_go = []

        global  result

        for dx, dy in directions:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if arr[x+dx][y+dy] == "0" and visited[x+dx][y+dy] == 0:
                    will_go.append((x+dx, y+dy))
                elif arr[x+dx][y+dy] =="3":
                    result = 1
                    return
        if will_go == [] : return
        else:
            for p in will_go:
                miro(*p)
    miro(*start)
    print(f"#{tc} {result}")