# 다익스트라

import heapq
n,m = map(int,input().split())
lst = [[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)


    


finresult = [0] * (n+1)
# 시작인덱스
for i in range(1,n+1):
    start = i
    inf = 21e8
    result = [inf] * (n+1)
    result[start] = 0
    pq = [(0,start)]
    while pq:
        price,ky = heapq.heappop(pq)
        if price > result[ky]: continue

        for do in lst[ky]:
            if result[do] > price + 1 :
                result[do] = price + 1
                heapq.heappush(pq,(price + 1, do))
    finresult[i] = sum(result[1:])
print(finresult.index(min(finresult[1:])))
