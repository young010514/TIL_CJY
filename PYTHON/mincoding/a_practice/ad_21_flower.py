import sys
sys.stdin = open("input/input_flower.txt","r")

def main(arr, n, p):
    # 우선 첫번째건 최대를 고르기

    ans = 0
    for i in range(0,n):
        first = arr[0][i]
        second = arr[1][i]
        if i ==0 :
            if first > second :
                ans += first
                prev = 1
            elif first < second :
                ans += second
                prev = 2
            else :
                ans += first
                prev = 0
            continue
        # 두번째 이후
        if prev == 1 : first -=p
        elif prev == 2 : second -= p
        else :
            first -=p
            second -= p


        if first > second :
            ans += first
            prev = 1
        elif first < second :
            ans += second
            prev = 2
        else :
            ans += first
            prev = 0
    return ans
T = int(input())
for tc in range(1,T+1):
    n,p = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(2)]
    print(main(arr,n,p))