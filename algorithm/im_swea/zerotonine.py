# import sys
# sys.stdin = open("input09.txt","r")

T = int(input())
for t in range(T):
    num = int(input())
    zr_to_nn = list(range(0,10))

    cnt = 0
    data = []
    while True:
        cnt += 1
        for i in list(str(num * cnt)):
            if int(i) not in data:
                data.append(int(i))
        data.sort()
        if data == zr_to_nn:
            break
    print(f"#{t+1} {num*cnt}")