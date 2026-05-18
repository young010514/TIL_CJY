import sys
sys.stdin = open("input/in_1263.txt",'r')

T=  int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    n = arr[0]
    print(n, len(arr))
    print(arr[1:18])
