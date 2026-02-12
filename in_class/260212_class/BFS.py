# 지금 내 현재 위치에서 이동 가능한 곳을 다 queue에 적어준다

from collections import deque
name = 'ABCDEF'

# 인접 행렬로 표현
arr = [
    [0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]

start = 0 # BFS 탐색 시작하는 인덱스

q = deque()
q.append(start)
while q :
    # 우선 now pop 하기
    now = q.popleft()
    print(name[now],end=' ')
    for i in range(6):
        if arr[now][i] == 1:
            q.append(i)


from collections import deque
name = 'ABCDEF'
print('\n\npractice')
# 인접 행렬로 표현
arr = [
    [0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]
start = 0
q= deque()
q.append(start)
while q:
    now=q.popleft()
    print(name[now],end=' ')
    for i in range(6):
        if arr[now][i]:
            q.append(i)

# 그래프 BFS 탐색 (모든 정점을 1번 씩만 탐색)
from collections import deque
name="ABCD"
arr=[
    [0,1,1,0],
    [0,0,0,1],
    [0,1,0,1],
    [0,0,0,0]]
used=[0]*4

def bfs(start):
    q=deque()
    q.append(start)
    while q:
        now=q.popleft()
        print(name[now],end=' ')
        for i in range(4):
            if arr[now][i]==1 and used[i]==0:
                used[i]=1
                q.append(i)
used[0]=1
bfs(0)
