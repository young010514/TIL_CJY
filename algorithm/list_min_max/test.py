import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    arr_len = int(input())
    arr = list(map(int,input().split()))
    max_data, min_data = arr[0], arr[0]
    for i in range(arr_len):
        if max_data < arr[i]:
            max_data = arr[i]
        if min_data > arr[i]:
            min_data = arr[i]
    print(f"#{t+1} {max_data-min_data}")
