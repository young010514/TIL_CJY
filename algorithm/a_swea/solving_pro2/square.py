import sys
sys.stdin = open("input_square.txt","r")

dts = [(0,1),(0,-1),(1,0),(-1,0)]
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result,cnt = 0,0
    


