import sys
sys.stdin =open("input/in_2117.txt")

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    houses = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] ==1 :houses.append((i,j))
    max_houses =0
    for i in range(n):
        for j in range(n):
            for k in range(1,n+2):
                cnt = 0
                for hr,hc in houses:
                    dist = abs(i-hr)+abs(j-hc)
                    if dist<k :
                        cnt += 1
                cost = k*k+(k-1)**2
                if cnt * m - cost >= 0 :
                    max_houses=max(cnt, max_houses)
    print(f'#{tc} {max_houses}')