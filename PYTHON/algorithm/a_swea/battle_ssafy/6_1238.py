import sys
sys.stdin = open("input_6.txt","r")

from collections import deque
for tc in range(1,11):
    n,start = map(int,input().split())
    arr = list(map(int,input().split()))
    nodes =[[] for _ in range(101)]
    visited = [0] * 101
    for i in range(n // 2):
        nodes[arr[i*2]].append(arr[i*2+1])

    q = deque()
    visited[start] = 1
    q.append((start,0)) # cnt
    end, enddata = 0,[]
    while q:
        now,cnt = q.popleft()
        if end < cnt :
            end = cnt
            enddata = [now]
        else: enddata.append(now)
        for i in nodes[now]:
            if visited[i] == 0 :
                visited[i] = 1
                q.append((i,cnt +1))
    result = max(enddata)
    print(f"#{ tc} {result}")
