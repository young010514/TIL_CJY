import sys
sys.stdin = open("input_special.txt","r")

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    sorted= False
    while sorted == False:
        sorted = True
        for i in range(N-1):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                sorted = False
    result = []
    for i in range(5):
        result.append(arr[-i-1])
        result.append(arr[i])
    print(f"#{t+1}", end=' ')
    print(*result)