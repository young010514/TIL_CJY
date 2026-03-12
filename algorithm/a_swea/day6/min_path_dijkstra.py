import sys
sys.stdin = open("input_minpath.txt","r")

import heapq
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    lines = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        lines[a].append((b,c))

    inf = 21e8
    result = [inf] * (n+1)
    result[0]=0
    heap = [(0,0)]  # cost, now
    while heap:
        cost, now = heapq.heappop(heap)
        for nxt,ky in lines[now]:
            if result[nxt] > cost + ky :
                result[nxt] = cost + ky
                heapq.heappush(heap,(cost+ky, nxt))

    print(f"#{tc} {result[-1]}")