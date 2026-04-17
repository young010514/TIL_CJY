import heapq
n,m,x = map(int,input().split())
lines =[[] for _ in range(n+1)]
lines_reverse =[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c= map(int,input().split())
    lines[a].append((b,c))
    lines_reverse[b].append((a,c))

def main(lines):
    q = [(0,x)] # cost
    inf = 1e8
    result = [inf] * (n+1)
    result[0], result[x] =0,0
    while q:
        cost,now = heapq.heappop(q)
        for nxt,nxtcost in lines[now]:
            if cost+nxtcost < result[nxt] :
                result[nxt] = cost+nxtcost
                heapq.heappush(q,(cost+nxtcost,nxt))
    return result
ret1= main(lines)
ret2= main(lines_reverse)
ans =[0] * (n+1)
for i in range(1,n+1):
    ans[i] = ret1[i] +ret2[i]
print(max(ans[1:]))