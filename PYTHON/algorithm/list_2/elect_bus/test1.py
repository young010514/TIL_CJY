import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def bus_stop(k,n,m, lst):
    now_loc, next_loc = 0,0

    result = 0
    while now_loc + k < n:
        for i in lst:
            if i - now_loc <= k :
                next_loc = i
                continue
            else:
                break
        if now_loc == next_loc :
            break
        now_loc = next_loc
        result += 1
    if now_loc + k < n : result = 0
    return result

for t in range(T) :
    k,n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    result = bus_stop(k,n,m, lst)
    print(f"#{t+1} {result}")