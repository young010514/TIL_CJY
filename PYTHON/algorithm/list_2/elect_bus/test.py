import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def bus_stop(arr, k, n, m):
    now_loc = 0
    cnt = 0
    for i in range(m):
        # 간격이 k를 넘기는 경우
        if arr[i] - now_loc > k :
            cnt = 0
            break
        # 두개 이상 점프하고 싶지만 마지막 인 경우:
        elif i == m-1 :
            if now_loc + k >= n:
                break
            else:
                cnt+= 1
                now_loc = arr[i]

        # 간격이 k를 넘기지 않고, 그 다음 간격이 k를 넘기는 경우
        elif arr[i+1] - now_loc > k  :
            cnt += 1
            now_loc = arr[i]

        elif arr[i+1] - now_loc <=k and now_loc + k < n:
            continue
        elif arr[i+1] - now_loc <=k and now_loc + k >= n:
            break


    if now_loc + k < n :
        cnt =0

    return cnt






for t in range(T):
    k,n,m = map(int,input().split())
    lst= list(map(int,input().split()))

    result = bus_stop(lst,k,n,m)
    print(f"#{t+1} {result}")

