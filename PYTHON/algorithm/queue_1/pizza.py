import sys
sys.stdin =open("input_pizza.txt","r")


from collections import deque
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    ci = list(map(int,input().split()))

    q =deque()

    for i in range(n):
        q.append([i,ci[i]])

    nextidx = n

    while q:

        nidx, ndata =q.popleft()
        ndata //=2

        if ndata !=0 :
            q.append([nidx,ndata])

        if ndata == 0 :
            if nextidx >= m:continue

            q.append([nextidx, ci[nextidx]])
            nextidx += 1

    result = nidx

    print(f"#{tc} {result+1}")