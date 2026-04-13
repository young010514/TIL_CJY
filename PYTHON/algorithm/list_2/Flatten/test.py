import sys
sys.stdin = open("input.txt", "r")

for t in range(1,11):
    n = int(input())
    arr= list(map(int,input().split()))
    for _ in range(n):
        max_idx, min_idx = arr.index(max(arr)), arr.index(min(arr))
        arr[max_idx] -= 1
        arr[min_idx] += 1

    print(f'#{t} {max(arr) - min(arr)}')