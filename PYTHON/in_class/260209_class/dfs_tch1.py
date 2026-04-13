# 3 4
# 9 9 9 1
# 1 9 1 1
# 1 1 1 1

# 간단 DFS 연습 문제 - 최대 합 경로(연속된 4칸 선택)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
selected = [(-1, -1)] * 4
Max = -21e8

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

high_val = 9  # 가지치기 (1~9사이의 정수가 들어온다고 가정)


def dfs(nowy, nowx, level, Sum):
    global Max

    # 앞으로 전부 가장 큰 값을 저장한다고 해도 Max를 못 넘는다면 리턴 (가지치기)
    if Sum + high_val * (3 - level) <= Max:
        return

    if level == 3:
        Max = max(Max, Sum)
        return

    for i in range(4):
        dy = nowy + directy[i]
        dx = nowx + directx[i]
        if dy < 0 or dy >= N or dx < 0 or dx >= M: continue
        if visited[dy][dx]: continue
        visited[dy][dx] = 1
        if level==1:
            dfs(nowy, nowx, level + 1, Sum + arr[dy][dx])
        dfs(dy,dx,level + 1, Sum + arr[dy][dx])
        visited[dy][dx] = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i,j,0, arr[i][j])
        visited[i][j] = 0

print(int(Max))
