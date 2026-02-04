import sys
sys.stdin = open("input_switch.txt", "r")

T = int(input())
for t in range(T):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int, input().split()))

    same = False
    cnt = 0
    while same == False:
        same = True
        for i in range(n):
            if arr1[i] != arr2[i]:
                arr1[i:] = [abs(data-1) for data in arr1[i:]]
                cnt += 1
    print(f"#{t+1} {cnt}")