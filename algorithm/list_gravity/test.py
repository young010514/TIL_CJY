import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    n = int(input())
    lst = list(map(int,input().split()))
    result = 0
    for i in range(n):
        cnt =0
        for j in range(i,n):
            if lst[i] > lst[j]:cnt += 1
        if cnt > result:
            result = cnt
    print(f"#{t+1} {result}")