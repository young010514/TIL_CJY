import sys
sys.stdin = open("input_max_count.txt","r")

T = int(input())
for _ in range(T):
    tc = int(input())
    lst= list(map(int,input().split()))
    arr = [0] *101
    for i in lst:
        arr[i] +=1
    idx = 100-arr[::-1].index(max(arr))
    print(f"#{tc} {idx}")