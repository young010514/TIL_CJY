import sys
sys.stdin = open("input_fly.txt","r")

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = -21e10
    for i in range(N):
        for j in range(N):

            datat, datax = -arr[i][j], - arr[i][j]

            for d in range(-M+1, M):
                # t 자 모양
                if 0 <= i + d <N: datat += arr[i+d][j]
                if 0 <= j + d <N: datat += arr[i][j+d]

                # x 자 모양
                if 0 <= i + d < N and 0 <= j+d < N : datax += arr[i + d][j+d]
                if 0 <= i + d < N and 0 <= j - d < N : datax += arr[i + d][j - d]

            result = max([result, datax, datat])
    print(f"#{t+1} {result}")

