import sys
sys.stdin = open("input_mincost.txt","r")

# 힙정렬로 풀어야하는거같음
import heapq
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    data = []    # sum, x,y
    heapq.heappush(data,(0,0,0))
    while data:
        Sum,x,y = heapq.heappop(data)
        if x == n-1 and y == n-1 :
            result = Sum
            break
        for i,j in directions:
            dx = x+i
            dy = y+j
            if dx <0 or dy <0 or dx >n-1 or dy>n-1 :continue
            heapq.heappush(data, (Sum + 1+ max(arr[dx][dy]-arr[x][y], 0), dx,dy))

    print(f"#{tc} {result}")