import sys
sys.stdin = open("input_region.txt","r")

from collections import deque

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n) ]
    person = list(map(int,input().split()))
    rawsum = sum(person)
    used = [0] * n
    Min = rawsum
    st = 0


    q =deque()
    used[0] = 1
    q.append([0,person[0]])
    while q:
        now, nowsum = q.popleft()
        if Min > abs(rawsum - 2*nowsum):
            Min = abs(rawsum -2 * nowsum)
        for i in range(n):
            if arr[now][i] == 1 and used[i] ==0 :
                used[i] = 1
                q.append([i,nowsum + person[i]])

    print(f"#{tc} {Min}")
