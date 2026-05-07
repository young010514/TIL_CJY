import sys
sys.stdin = open("input/in_1868.txt", "r")

from collections import deque

dts = [(-1, -1), (-1, 0), (-1, 1),
       (0, -1),           (0, 1),
       (1, -1),  (1, 0),  (1, 1)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for dx, dy in dts:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if visited[nx][ny]:
                continue

            if board[nx][ny] == '*':
                continue

            visited[nx][ny] = True

            # 0인 칸만 계속 확장
            if board[nx][ny] == 0:
                q.append((nx, ny))


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    board = [list(input()) for _ in range(n)]

    # 숫자 맵으로 변환
    for i in range(n):
        for j in range(n):

            if board[i][j] == '*':
                continue

            cnt = 0

            for dx, dy in dts:
                nx = i + dx
                ny = j + dy

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if board[nx][ny] == '*':
                    cnt += 1

            board[i][j] = cnt

    visited = [[False] * n for _ in range(n)]

    ans = 0

    # 0 영역 먼저 BFS
    for i in range(n):
        for j in range(n):

            if board[i][j] == 0 and not visited[i][j]:
                bfs(i, j)
                ans += 1

    # 남은 숫자 칸 처리
    for i in range(n):
        for j in range(n):

            if board[i][j] != '*' and not visited[i][j]:
                ans += 1

    print(f"#{tc} {ans}")