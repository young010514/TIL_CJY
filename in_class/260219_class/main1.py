# 위상정렬 (topology sort) - 작업 순서 선수과목 공정순서 등

name = ['a','b','c','d','e','f','g']

arr = [
    [0,0,0,0,0,1,0],
    [0,0,1,1,0,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0],
]
from collections import deque

q = deque()
acc = [0] * 7
used = [0] * 7

# 사전 작업개수 등록
for j in range(7):
    for i in range(7):
        if arr[i][j]==1:
            acc[j]+=1

# 바로 작업 착수 가능한것들은 큐에 넣고 used 1체크
for i in range(7):
    if acc[i]==0:
        used[i]=1
        q.append(i)

# 큐에서 작업 가능한것들 하나씩 수행하기
while q:
    now=q.popleft()
    print(name[now],end=' ')
    for i in range(7):
        if acc[i]==1:
            used[i]=1
            acc[i]-=1
            q.append(i)
        else:
            acc[i]-=1


