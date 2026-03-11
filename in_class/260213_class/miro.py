# 미로찾기
# 강사님 풀이
# 0,0,0,0
# 1,0,1,1
# 1,0,1,0
# 0,0,0,0

# 0,0 에서 출발해서 3,3까지 도착하고자 한다.
# 도착이이 가능한지 불가능 한지 출력해 주세요

from collections import deque
arr=[
    [0,0,0,0],
    [1,0,1,1],
    [1,0,1,0],
    [0,0,0,0],
]
directy=[0,0,-1,1]
directx=[-1,1,0,0]
visited=[[0]*4 for _ in range(4)]
visited[0][0]=1

q=deque()
q.append((0,0)) # 탐색 시작 좌표를 큐에 넣고 탐색ㄱㄱ

flag=0
while q:
    nowy,nowx=q.popleft()
    for i in range(4):
        dy=nowy+directy[i]
        dx=nowx+directx[i]
        if dy<0 or dx<0 or dy>3 or dx>3: continue # 배열범위 체크
        if arr[dy][dx]==1 or visited[dy][dx]==1: continue # 벽이거나 방문한 적이 있다면
        visited[dy][dx]=1
        q.append((dy,dx))
        if dy==3 and dx==3:
            flag=1
            break
    if flag:
        break
if flag:
    print("도착가능")
else:
    print('도착 불가능')




# 미로찾기

# 0,0,0,0
# 1,0,1,0
# 1,0,1,0
# 0,0,0,0

# 0,0 에서 출발해서 3,2까지 도착하고자 한다.
# 최소 이동 거리를 출력해 주세요

from collections import deque
arr=[
    [0,0,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0],
]

used=[[0]*4 for _ in range(4)]
q=deque()
used[0][0] == 1
q.append((0,0,0)) # x,y,거리
direcitons = [(0,1),(0,-1),(1,0),(-1,0)]

# Min = 100
while q:
    nowx,nowy, data = q.popleft()
    if nowx == 3 and nowy == 2 :
        print(data)
        # 이것도 굳이 필요가 없음!    if Min > data : Min = data
    for i,j in direcitons:
        dx = nowx+i
        dy = nowy+j
        if dx <0 or dy <0 or dx > 3 or dy > 3 :continue
        if used[dx][dy] ==1 or arr[dx][dy] == 1: continue
        used[dx][dy] = 1
        q.append((dx,dy,data+1))

# print(Min)


# ===============================================



















