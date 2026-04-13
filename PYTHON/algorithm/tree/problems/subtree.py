import sys
sys.stdin = open("input_subtree.txt","r")

T = int(input())
for tc in range(1,T+1):
    e,n = map(int,input().split())

    left = [0] * (e+2)
    right = [0] * (e+2)
    lines = list(map(int,input().split()))
    for i in range(e):
        par = lines[2*i]
        low = lines[2*i+1]
        if left[par] == 0: left[par] = low
        else:right[par] = low

    from collections import deque
    # root = n
    cnt = 0
    q= deque()
    q.append(n)
    while q:
        now = q.popleft()
        cnt +=1
        if left[now] != 0 : q.append(left[now])
        if right[now] != 0 : q.append(right[now])
    print(f"#{tc} {cnt}")