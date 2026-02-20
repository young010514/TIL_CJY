import sys
sys.stdin = open("input_pw.txt","r")

from collections import deque
for _ in range(10):
    tc = int(input())
    lst = deque(map(int,input().split()))
    gap = 1
    while 1:
        now = lst.popleft()
        nxt = now - gap
        if nxt <= 0:
            lst.append(0)
            break
        lst.append(nxt)
        if gap == 5: gap = 1
        else: gap += 1
    print(f"#{tc}",*lst)