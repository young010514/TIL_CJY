import sys
sys.stdin = open("input_minsum.txt","r")

import heapq

def main(n, arr):
    # 우선순위 큐를 위한 최소 힙
    pq = []
    # 최소 비용 배열, 모든 값은 무한대로 초기화
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = arr[0][0]  # 시작점 초기화

    # (누적 비용, x, y)
    heapq.heappush(pq, (arr[0][0], 0, 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향

    while pq:
        current_dist, x, y = heapq.heappop(pq)

        # 목표 지점에 도달하면 그때의 비용이 최소값
        if x == n - 1 and y == n - 1:
            return current_dist

        # 네 방향으로 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 범위 밖으로 나가면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 새로운 경로 비용 계산
            new_dist = current_dist + arr[nx][ny]

            # 더 작은 비용으로 갱신되면 우선순위 큐에 추가
            if new_dist < dist[nx][ny]:
                dist[nx][ny] = new_dist
                heapq.heappush(pq, (new_dist, nx, ny))


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    rst = main(n,arr)
    print(f"#{tc} {rst}")
