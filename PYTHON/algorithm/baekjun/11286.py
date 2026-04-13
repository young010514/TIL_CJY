import heapq

N = int(input())
heap = []
for n in range(N):
    x = int(input())
    if x != 0 :
        heapq.heappush(heap,(abs(x),x))
    else:
        if heap :
            _,data = heapq.heappop(heap)
            print(data)
        else:print(0)