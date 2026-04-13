import sys
sys.stdin = open("input_bus.txt","r")

from collections import deque
T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    q = deque()
    q.append((1,arr[1], 0))     # 현재 위치, 충전, cnt
    while q:
        now, charge, cnt = q.popleft()
        if now + charge >= arr[0] :
            result = cnt
            break
        for i in range(1,charge+1):
            q.append((now + i, arr[now+i], cnt +1 ))
    print(f"#{tc} {result}")
