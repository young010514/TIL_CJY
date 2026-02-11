import sys
sys.stdin = open("input_onoff.txt","r")

N = int(input())
lst = list(map(int,input().split()))
s_num = int(input())
for i in range(s_num):
    x,y = map(int,input().split())
    # 남자
    if x == 1 :
        num = y - 1
        while num  < N:
            lst[num] = 1-lst[num]
            num += y
    else:
        gap = 0
        while 1:
            if y-gap <0 or y + gap >= N :
                gap -= 1
                break
            if lst[y + gap] == lst[y-gap] : gap +=1
            else:
                gap -= 1
                break
        for i in range(-1*gap, gap + 1):
            lst[y+i] = 1-lst[y+i]
print(*lst)