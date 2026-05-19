import sys
sys.stdin= open("input/in_2105.txt","r")




T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dts = [(1,-1),(1,1),(-1,1),(-1,-1)]  # 반시계 방향으로 회전
    for i in range(n-2):
        for j in range(1,n-1):
            st = (i,j) # 시작 지점을 사각형 위쪽으로 잡기
