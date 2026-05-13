import sys
sys.stdin =open("input/in_2117.txt")

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
