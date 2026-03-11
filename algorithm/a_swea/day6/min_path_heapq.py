import sys
sys.stdin = open("input_minpath.txt","r")

import heapq
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    lines = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        heapq.heappush()
    heapq.heapify(lines)
    print(lines)

    result = 2e10




    print(f"#{tc} {result}")