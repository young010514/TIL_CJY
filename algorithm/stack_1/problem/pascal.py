import sys
sys.stdin = open("input_pascal.txt","r")

T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    # print(arr)
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i or i == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
    print(f"#{t}")
    for inner in arr:
        for x in inner:
            if x != 0 :print(x,end=' ')
        print()









