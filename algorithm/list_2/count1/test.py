import sys
sys.stdin = open("input.txt","r")

T = int(input())
for t in range(T):
    n = int(input())
    lst = list(map(int,list(input())))
    result = []
    cnt = 0
    for i in lst:
        if i == 1:
            cnt += 1
            result.append(cnt)
        else:
            cnt = 0

    print(f"#{t+1} {max(result)}")