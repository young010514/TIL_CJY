import sys
sys.stdin = open("input_draw.txt","r")

T= int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = []
    for i in range(n) :
        for j in range(n):
            for x in range(i,n):
                for y in range(j,n):
                    if arr[i][j] == arr[x][y] : result.append((x-i+1) *(y-j+1) )
    print(f'#{tc} {result.count(max(result))}')