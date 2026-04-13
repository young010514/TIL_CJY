# n,m 입력
# n*m 사이즈의 배열에 정수값 입력
# 연속된 4칸을 선택했을때 가장 합이 클 경우, 그 합은 몇일까요?

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
selected = [(-1, -1)] * 4  # 선택된 좌표 저장 (최대 4칸)
Max = -21e8

directy=[-1,1,0,0]
directx=[0,0,-1,1]

high_val = 9  # 가지치기 (1~9사이의 정수가 들어온다고 가정)

def dfs(level, total_sum, start_idx):
    global Max

    # 앞으로 전부 가장 큰 값을 저장한다고 해도 Max를 못 넘는다면 리턴 (가지치기)
    if total_sum + high_val * (3 - level) <= Max: return


    if level == 3:  # 총 selected 배열에 총 4개의 숫자가 선택되었을때
        Max = max(Max, total_sum)
        return

    # 현재까지 선택된 모든 칸에서 확장해보기
    for k in range(level + 1):
        y, x = selected[k]
        for i in range(4):
            dy=y+directy[i]
            dx=x+directx[i]
            if dy < 0 or dy >= N or dx < 0 or dx >= M: continue
            if visited[dy][dx]: continue

            index=dy*M+dx
            if index<start_idx: continue #탐색 시작 인덱스가 start_idx보다 작으면 continue를 통해, 중복탐색 줄이기

            visited[dy][dx] = 1
            selected[level + 1] = (dy, dx)
            print(selected)
            dfs(level + 1, total_sum + arr[dy][dx],start_idx)
            visited[dy][dx] = 0
            selected[level + 1] = (-1, -1)

# 모든 칸을 시작점으로 시도
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        selected[0] = (i, j)
        start_idx = i * M + j # 이차원 배열의 좌표를 정수값으로 표현하는 방식임
        dfs(0, arr[i][j],start_idx)
        visited[i][j] = 0

print(Max)
