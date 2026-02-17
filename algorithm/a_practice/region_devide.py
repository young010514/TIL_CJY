import sys
sys.stdin = open("input_region.txt","r")

from collections import deque

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n) ]
    person = list(map(int,input().split()))
    
    def bfs():
        return




    print(f"#{tc} ")
