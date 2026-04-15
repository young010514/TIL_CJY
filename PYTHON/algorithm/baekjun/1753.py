import heapq
v,e = map(int,input().split())
start = int(input())
lines = [[] for _ in range(1+v)]
for _ in range(e):
    st,ed,w = map(int,input().split())
    lines[st].append((ed, w))

visited = [0] * (v+1)
visited[start] = 1

inf = 1e9
result = [inf] * (v+1)
result[start] = 0
q = [(0,start)] # cost, now
while q:
    cost, now = heapq.heappop(q)

    if cost > result[now] :continue

    for nxt, w in lines[now]:
        if w + cost < result[nxt] :
            result[nxt] = w+cost
            heapq.heappush(q,(cost+w, nxt))

for i in range(1,v+1):
    if result[i] == inf:
        print("INF")
    else:print(result[i])