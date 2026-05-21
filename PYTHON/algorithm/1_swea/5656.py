import sys
sys.stdin = open("input/in_5656.txt","r")

T = int(input())
for tc in range(1,T+1):
    n,w,h = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(h)]

