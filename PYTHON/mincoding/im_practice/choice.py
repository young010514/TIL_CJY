import sys
sys.stdin = open("input_choice.txt","r")

T = int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    result = 0
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            data = lst[j:j+i]
            if data[-1] - data[0] <= k:
                if i > result:
                    result = i
                    break
    print(f"#{tc} {result}")