import sys
sys.stdin = open("input_bogeup.txt","r")

import heapq
dts = [(0,1),(0,-1),(1,0),(-1,0)]
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,list(input()))) for _ in range(n)]

    ans = 21e8
    result = [[21e8] * n for _ in range(n)]
    result[0][0] = 0
    heap = [(0,0,0,0)]  # cost, (heap정렬을 위한 -(x+y) 값), 좌표값
    while heap:
        cost, _ ,x,y = heapq.heappop(heap)
        if x == n-1 and y == n-1 :
            ans = cost
            break

        for i,j in dts:
            dx = x +i
            dy = y +j
            if dx <0 or dy < 0 or dy >n-1 or dx > n-1 : continue
            if result[dx][dy] > cost + arr[dx][dy] :
                result[dx][dy] = cost + arr[dx][dy]
                heapq.heappush(heap, (cost+arr[dx][dy], -dx-dy, dx,dy))
    print(f"#{tc} {ans}")

