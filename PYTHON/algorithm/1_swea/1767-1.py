import sys
sys.stdin = open("input/in_1767.txt", "r")

dts = [(-1,0),(1,0),(0,-1),(0,1)]

def can_connect(x, y, dx, dy):
    nx, ny = x + dx, y + dy
    length = 0

    while 0 <= nx < N and 0 <= ny < N:
        if arr[nx][ny] != 0:
            return 0

        nx += dx
        ny += dy
        length += 1

    return length


def set_line(x, y, dx, dy, value):
    nx, ny = x + dx, y + dy
    length = 0

    while 0 <= nx < N and 0 <= ny < N:
        arr[nx][ny] = value
        nx += dx
        ny += dy
        length += 1

    return length


def dfs(idx, connected, wire_len):
    global max_core, min_wire

    # 모든 코어 처리 완료
    if idx == len(cores):

        if connected > max_core:
            max_core = connected
            min_wire = wire_len

        elif connected == max_core:
            min_wire = min(min_wire, wire_len)

        return

    x, y = cores[idx]

    connected_flag = False

    # 4방향 연결 시도
    for dx, dy in dts:

        length = can_connect(x, y, dx, dy)

        if length:

            set_line(x, y, dx, dy, 2)

            dfs(idx + 1,
                connected + 1,
                wire_len + length)

            set_line(x, y, dx, dy, 0)

            connected_flag = True

    # 연결 안 하는 경우
    dfs(idx + 1, connected, wire_len)


T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    cores = []

    # 가장자리 제외
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] == 1:
                cores.append((i, j))

    max_core = 0
    min_wire = float('inf')

    dfs(0, 0, 0)

    print(f"#{tc} {min_wire}")