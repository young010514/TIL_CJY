import sys
sys.stdin =open("input_bee_1.txt","r")

T = int(input())
for tc in range(1,T+1):

    n,m = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(n)]
    used = [[0] * m for _ in range(n)]
    # j 가 짝수일 경우
    dir1= [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1)]
    # j 가 홀수일 경우
    dir2 = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1)]

    Max = 0

    # 한 점을 시작으로 이동하는 경우
    def bee(level,  Sum, x,y):
        global  Max
        if level == 4:
            if Sum > Max :Max = Sum
            return

        # 위치에 따라 갈수 있는 범위 다름
        if y % 2 == 0 :
            directions = dir1
        else:
            directions = dir2

        for i,j in directions:
            dx = x + i
            dy = y + j
            if dx <0 or dy < 0 or dx >= n or dy >= m:continue
            if used[dx][dy] == 1 :continue

            used[dx][dy] =1
            # 한점을 기준으로 전진하는 경우
            bee(level+1,Sum + arr[dx][dy],dx,dy)
            # 한 점을 기준으로 둘러싼 경우
            bee(level + 1, Sum + arr[dx][dy], x, y)
            used[dx][dy] =0

    for a in range(n):
        for b in range(m):
            used[a][b] = 1
            bee(1,arr[a][b],a,b)
            used[a][b] = 0

    print(f"#{tc} {Max}")