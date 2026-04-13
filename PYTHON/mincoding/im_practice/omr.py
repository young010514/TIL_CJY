import sys
sys.stdin =open("input_omr.txt","r")

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    ans = list(map(int,input().split()))
    stlst = [list(map(int,input().split())) for _ in range(n)]
    bnlst = [[0] * m for _ in range(n)]
    for i in range(n):
        bnlst[i][0] = int(ans[0] == stlst[i][0])
        for j in range(1,m):

            if stlst[i][j] != ans[j] :
                bnlst[i][j] = 0
            else : bnlst[i][j] = bnlst[i][j-1] + 1

    Max,Min = 0,1000
    for i in range(n):
        Sum = sum(bnlst[i])
        if Sum < Min: Min = Sum
        if Sum > Max: Max = Sum
    print(f"#{tc} {Max-Min}")


