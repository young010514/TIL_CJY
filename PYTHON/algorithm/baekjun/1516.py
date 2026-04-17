from collections import deque
n = int(input())
cnt = [0] * (n+1)
acc =[[] for _ in range(n+1)]
cost = [0] * (n+1)

for i in range(1,1+n):
    arr = list(map(int,input().split()))
    cost[i] = arr[0]
    lst = deque(arr[1:])
    while lst:
        now = lst.popleft()
        if now == -1 : break
        cnt[i] += 1
        acc[now].append(i)
result = [0] * (n+1)
q= deque()
for i in range(n+1):
    if cnt[i] == 0:
        result[i] = cost[i]
        q.append(i)
while q:
    now = q.popleft()
    for nxt in acc[now]:
        cnt[nxt] -= 1

        # 핵심: max로 갱신
        result[nxt] = max(result[nxt], result[now] + cost[nxt])

        if cnt[nxt] == 0:
            q.append(nxt)

for i in range(1,n+1):
    print(result[i])