import sys

sys.stdin = open('input.txt', 'r')


def solve(tc):
    n, m = map(int, input().split())
    farming = [list(map(int, input().split())) for _ in range(n)]
    diry = [0, 1, 0, -1]
    dirx = [1, 0, -1, 0]

    def FindMax(sty, stx, std):
        harvest = [[0] * n for _ in range(n)]  # 곡식이 열리는 날짜 저장
        seed = [[0] * n for _ in range(n)]  # 씨를 몇 번 심었는지
        total = 0
        y, x, d = sty, stx, std
        # 로봇이 m일동안 일함
        for day in range(1, m + 1):
            # --준비: 다음 칸으로 이동 가능 여부 확인--
            can_move = False
            for i in [1, 0, 3, 2]:
                nxtd = (d + i) % 4
                nxty, nxtx = y + diry[nxtd], x + dirx[nxtd]
                if nxty < 0 or nxty >= n or nxtx < 0 or nxtx >= n: continue  # 배열 범위를 벗어나면 continue
                if farming[nxty][nxtx] == 1: continue  # 장애물이 있는 경우 못감
                if harvest[nxty][nxtx] == 0 or day >= harvest[nxty][nxtx]:
                    can_move = True
                    ty, tx, td = nxty, nxtx, nxtd
                    break

            # --오전 업무--
            # 수확
            if harvest[y][x] != 0 and day >= harvest[y][x]:  # 곡식이 열리면, 현재 위치에서 수확
                total += 1
                harvest[y][x] = 0
            # 씨 심기
            elif can_move and harvest[y][x] == 0:
                seed[y][x] += 1  # 씨를 심은 횟수 저장
                harvest[y][x] = day + 1 + 3 + seed[y][x]
            # --오후 업무--
            if can_move:
                y, x, d = ty, tx, td  # 내일 이동할 곳
        return total

    max_farm = 0
    for i in range(n):
        for j in range(n):
            if farming[i][j] != 1:
                for k in range(4):
                    result = FindMax(i, j, k)
                    max_farm = max(max_farm, result)

    print(f'#{tc}', max_farm)


T = int(input())
for tc in range(1, T + 1):
    solve(tc)