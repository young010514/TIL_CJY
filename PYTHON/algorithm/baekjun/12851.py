from collections import deque

a, b = map(int, input().split())

MAX = 100001
dist = [-1] * MAX  # 해당 위치까지 최소 시간
cnt = [0] * MAX    # 해당 위치까지 오는 경우의 수

q = deque()
q.append(a)
dist[a] = 0
cnt[a] = 1

while q:
    now = q.popleft()

    for nxt in (now - 1, now + 1, now * 2):
        if 0 <= nxt < MAX:
            # 처음 방문
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                cnt[nxt] = cnt[now]
                q.append(nxt)

            # 같은 최단 시간으로 다시 도달
            elif dist[nxt] == dist[now] + 1:
                cnt[nxt] += cnt[now]

print(dist[b])
print(cnt[b])