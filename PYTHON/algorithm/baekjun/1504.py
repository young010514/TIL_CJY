import heapq
n,e=map(int,input().split())
lines=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    lines[a].append((b,c))
    lines[b].append((a,c))
result = -1
x,y = map(int,input().split())
def line(to):
    dist = [1e9] * (n+1)
    dist[to] = 0
    q = [(0, to)]

    while q:
        ncost, now = heapq.heappop(q)

        if ncost > dist[now]:
            continue

        for nxt, c in lines[now]:
            new_cost = ncost + c
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))
    return dist
l1 = line(1)
lx = line(x)
ln = line(n)
data = [l1[x], l1[y],lx[y],ln[x],ln[y]]
result = min(data[0] + data[4], data[1]+ data[3]) + data[2]
if result>=1e9 : result = -1
print(result)