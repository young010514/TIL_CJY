import sys
sys.stdin = open("input/in_1244.txt","r")


def dfs(a,l,b,now):
    if now == b :

        global Max
        test = False
        for i in range(l):
            if Max[i] == a[i]: continue
            elif Max[i] < a[i] :
                test= True
                break
            else:
                break
        if test:
            Max = a[:]

        return
    for i in range(l-1):
        for j in range(i+1,l):
            a[i], a[j] = a[j],a[i]
            dfs(a,l,b,now+1)
            a[i], a[j] = a[j],a[i]

T = int(input())
for tc in range(1,T+1):
    a,b = input().split()
    a = list(map(int,list(a)))
    b= int(b)
    Max = a[:]

    dfs(a,len(a),b,0)
    print(f'#{tc}', end=' ')
    [print(i,end= '') for i in Max]
    print()