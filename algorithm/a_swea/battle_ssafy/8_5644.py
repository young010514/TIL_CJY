import sys
sys.stdin = open("input_8.txt","r")

T = int(input())
for tc in range(1,T+1):
    m,a = map(int,input().split())
    arr = [[0] * 11 for _ in range(11)]
    usera = list(map(int,input().split()))
    userb = list(map(int,input().split()))
    for _ in range(a):
        x,y,c,p = map(int,input().split())