import sys
sys.stdin =open("input_stone.txt","r")

T = int(input())
for tc in range(1,T+1):
    m,n = map(int,input().split())
    lst = list(map(int,input().split()))
    data = [tuple(map(int,input().split())) for _ in range(n)]
    for i, j in data:
        # print(i,j)
        mid = i-1
        for x in range(1,j+1):
            if mid -x < 0 or mid + x >= m:
                break
            if lst[mid-x] == lst[mid+x] :
                lst[mid-x] = 1- lst[mid-x]
                lst[mid+x] = 1- lst[mid+x]
    print(f"#{tc}", end=' ')
    print(*lst)