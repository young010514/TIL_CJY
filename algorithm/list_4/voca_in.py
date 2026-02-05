import sys
sys.stdin = open("input_voca.txt","r")

T = int(input())
for t in range(T):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        cnt1, cnt2 = 0,0
        for j in range(N):
            if arr[i][j] ==1 :
                cnt1 += 1
            elif arr[i][j] == 0:
                result.append(cnt1)
                cnt1=0
            if arr[j][i] == 1:
                cnt2 += 1
            elif arr[j][i] == 0:
                result.append(cnt2)
                cnt2 = 0
            if j == N-1 :
                result.append(cnt1)
                result.append(cnt2)
    data = result.count(K)
    print(f"#{t+1} {data}")