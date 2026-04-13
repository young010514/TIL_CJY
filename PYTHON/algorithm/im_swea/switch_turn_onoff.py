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
        num = y-1
        gap = 0
        while 1:
            if num-gap <0 or num + gap >= N :
                gap -= 1
                break
            elif lst[num + gap] == lst[num-gap] : gap +=1
            else:
                gap -= 1
                break
        for i in range(-1*gap, gap + 1):
            lst[num+i] = 1-lst[num+i]

if N > 20:
    start = 0
    data = lst[:20]
    while data :
        for x in data:
            print(x,end=' ')
        print()
        start += 1
        data = lst[20*start:20*(start+1)]

else:
    for i in lst:
        print(i,end=' ')