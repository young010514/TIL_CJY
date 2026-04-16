import heapq
n = int(input())
m = int(input())
lines = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,cost = map(int,input().split())
    lines[s].append((e,cost))
st,ed = map(int,input().split())
inf = 1e9
def cost(st, ed):
    result = [inf] * (n+1)
    q = [(0,st)]   # cost, now
    result[st] = 0
    while q:
        cost, now = heapq.heappop(q)
        if cost > result[now] :continue
        for nxt,c in lines[now]:
            if result[nxt] <= cost+c : continue
            result[nxt] = cost+c
            heapq.heappush(q,(cost+c, nxt))
    return result[ed]
print(cost(st,ed))

