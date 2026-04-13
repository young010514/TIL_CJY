# 개선 후 다익스트라

import heapq
inf = 21e8
n,m = map(int,input().split())
lst = [[] for _ in range(n)]
for _ in range(m):
    a,b,c= map(int,input().split())
    lst[a].append((b,c))
# 시작인덱스
start = 0
result = [inf] * 5
result[start] = 0
pq = [(0,start)]
while pq:
    price,ky = heapq.heappop(pq)
    if price > result[ky]: continue

    for do,do_cost in lst[ky]:
        if result[do] > price + do_cost :
            result[do] = price + do_cost
            heapq.heappush(pq,(price + do_cost, do))
print(result)



















