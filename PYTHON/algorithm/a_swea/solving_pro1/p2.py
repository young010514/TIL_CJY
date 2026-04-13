import sys
sys.stdin = open("input_p2.txt",  "r")

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            a,b = arr[i]
            c,d = arr[j]
            if (a-c) * (b-d) < 0 : ans += 1
    print(f"#{tc} {ans}")




