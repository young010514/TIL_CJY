import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    n, m = map(int,input().split())
    lst = list(map(int,input().split()))
    max_data, min_data =0,0
    for x in range(m):
        max_data += lst[x]
        min_data += lst[x]

    for i in range(n-m + 1):
        s = 0
        for j in range(m):
            s += lst[i+j]
        if s > max_data : max_data = s
        if s < min_data : min_data = s
    print(f"#{t+1} {max_data - min_data}")