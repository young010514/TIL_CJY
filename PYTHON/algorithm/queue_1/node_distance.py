import sys
sys.stdin =open("input_distance.txt","r")

from collections import  deque
from copy import deepcopy
T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    arr= [list(map(int,input().split())) for _ in range(e)]
    s,g =map(int,input().split())

    # print(v,e)
    # print(arr)
    # print(s,g)
    Min = 1000

    q = deque()
    q.append((s, 0, [s])) # 노드, 경로, 거리
    while q:
        node, dist, how = q.popleft()
        if node == g and Min > dist : Min  = dist


        for i in range(e):
            for j in range(2) :
                if arr[i][j] == node and arr[i][1-j] not in how:
                    next_how = deepcopy(how)
                    next_how.append(arr[i][1-j])
                    q.append((i, next_how, dist+1))


    if Min == 1000 :Min = 0
    print(f"#{tc} {Min}")