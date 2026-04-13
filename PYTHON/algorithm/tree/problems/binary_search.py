import sys
sys.stdin = open("input_binary.txt","r")



T = int(input())
for tc in range(1,T+1):
    n = int(input())
    data = [0] * (n+1)

    i = 1
    def in_order(now):
        global i
        if 0< now < n+1:
            in_order(2*now)
            data[now] = i
            i += 1
            in_order(2*now+1)
    in_order(1)

    print(f"#{tc} {data[1]} {data[n//2]}")