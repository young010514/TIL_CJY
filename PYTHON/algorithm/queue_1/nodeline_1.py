import sys
sys.stdin =open("input_nodeline.txt","r")

from collections import deque
T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(e)]
    s,g = map(int,input().split())
    nodes = list(range(1,v+1))
    # 사이클 방지를 위한 used 리스트
    used =[0] * (v+1)
    # 결과 담을 result
    result = 0
    q = deque()
    used[s] = 1
    q.append((s,0))
    while q:
        now,lth = q.popleft()
        if now == g :
            result = lth
            break
        for i in range(e):
            if now not in lst[i]: continue
            nxt = lst[i][1-lst[i].index(now)]
            if used[nxt] == 0:
                used[nxt] = 1
                q.append((nxt,lth+1))

    print(f"#{tc} {result}")