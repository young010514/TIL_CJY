import sys
sys.stdin = open("input_radius.txt","r")

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n+1)]

    lst1= []
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j] == 0 :continue
            if arr[i][j] == 1 : lst1.append((i,j))
            if arr[i][j] == 2 : px,py = i,j
    Max = 0
    for i,j in lst1:
        data= (i-px) ** 2 + (j-py) ** 2
        if data > Max : Max = data

    R = Max ** 0.5
    if R % 1== 0 :
        R = int(R)
    else:R = int(R) + 1

    print(f"#{tc} {R}")
