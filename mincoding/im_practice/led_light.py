import sys
sys.stdin=open("input_light.txt","r")

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst = list(map(int,input().split()))
    raw = [0] * n
    cnt =0
    bn = True
    while bn:
        bn = False
        for i in range(n):
            if lst[i] != raw[i] :
                x = i
                bn=True
                cnt += 1
                while x < n:
                    raw[x] = 1-raw[x]
                    x += i+1
                break

    print(f"#{tc} {cnt}")