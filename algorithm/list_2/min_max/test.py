import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int,input().split()))
    min_data, max_data = lst[0], lst[0]
    min_idx, max_idx = 0,0
    for idx, data in enumerate(lst):
        if data < min_data:
            min_idx, min_data = idx, data
        if data >= max_data:
            max_idx, max_data = idx, data
    print(f"#{t+1} {abs(max_idx-min_idx)}")
