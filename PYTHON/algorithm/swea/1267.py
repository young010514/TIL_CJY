import sys
sys.stdin = open("input/1267_input.txt","r")



for tc in range(1,11):
    v,e = map(int,input().split())
    arr = list(map(int,input().split()))
    acc =[[] for _ in range(v+1)]
    cnt = [0] *(v+1)
    for i in range(e):
        x = arr[2*i]
        y = arr[2*i+1]
        cnt[y] += 1
        acc[x].append(y)
    used = 0
    print(f"#{tc}",end=' ')
    while 1:
        if used == v : break
        for i in range(1,v+1):
            if cnt[i] == 0:
                print(i, end=' ')
                cnt[i] -= 1
                used += 1
                for nxt in acc[i]:
                    cnt[nxt] -= 1
    print()