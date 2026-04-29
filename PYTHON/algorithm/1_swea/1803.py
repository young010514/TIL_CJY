import sys
sys.stdin = open("input/in_1803.txt",'r')

import heapq

def main(n,st,ed,arr):
    result = [1e15] * (n+1)
    result[st] = 0
    q = [(0,st)]
    while q:
        nc,now = heapq.heappop(q)
        for nxt, cost in arr[now]:
            if result[nxt] < nc + cost: continue
            result[nxt] = nc + cost
            # q.append((nxt,nc+cost))
            heapq.heappush(q,(nc+cost,nxt))
    return result[ed]

T= int(input())
for tc in range(1,T+1):
    n,m,st,ed = map(int,input().split())
    lines = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        lines[a].append((b,c))
        lines[b].append((a,c))
    ans = main(n,st,ed,lines)
    print(f'#{tc} {ans}')
