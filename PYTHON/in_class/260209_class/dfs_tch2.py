N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
Max = -21e8

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

high_val = 9  # 가지치기 (1~9사이의 정수가 들어온다고 가정)

def dfs(y,x,level, Sum):
    global Max

    # 앞으로 전부 가장 큰 값을 저장한다고 해도 Max를 못 넘는다면 리턴 (가지치기)
    if Sum + high_val * (3 - level) <= Max: return

    if level == 3:
        Max = max(Max, Sum)
        return

    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy < 0 or dy >= N or dx < 0 or dx >= M: continue
        if visited[dy][dx]: continue
        visited[dy][dx] = 1
        dfs(dy,dx,level + 1, Sum + arr[dy][dx])
        visited[dy][dx] = 0

# dfs
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i,j,0, arr[i][j])
        visited[i][j] = 0


# ㅗ 모양만 따로 처리 (+ 십자가 모양으로 다 더한다음, 위,아래,좌,우 중 가장 작은값 빼기)

for y in range(N):
    for x in range(M):
        around = []  # 위,아래,좌,우 값 저장할 배열
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dx < 0 or dy >= N or dx >= M: continue
            around.append(arr[dy][dx])

        # ㅗ모양은 최소 3방향이 있어야 가능함
        if len(around) < 3: continue
        total=arr[y][x]+sum(around)

        # 4방향이 저장되었다면, 4방향 중 가장 작은 값 하나 빼기
        if len(around) == 4:
            total -= min(around)
        Max = max(Max, total)
print(Max)
