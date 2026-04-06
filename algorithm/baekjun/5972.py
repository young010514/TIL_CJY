import heapq
n,m=map(int,input().split())
lines = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    lines[a].append((b,c))
    lines[b].append((a,c))
q= [(0, 1)]  # sum, now node
result = [8e8] * (n+1)
result[1] = 0
while q:
    cost, now = heapq.heappop(q)
    if cost > result[now] :continue

    for x,y in lines[now]:
        if result[x] > cost + y:
            result[x] = cost+y
            heapq.heappush(q,(cost + y, x))
print(result[n])