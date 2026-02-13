# for 문을 통해
from collections import deque
arr = [
    [0,0,0,0,1,0],
    [0,1,0,0,0,0],
    [1,1,1,0,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,0,0]
]
directions = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(stx,sty,edx,edy):
    used = [[0]*6 for _ in range(5)]
    used[stx][sty] =1
    q=deque()
    q.append((sty,stx,0))
    while q :
        x,y,cnt = q.popleft()
        if x == edx and y == edy :
            return cnt
        for i,j in directions :
            dx = x+i
            dy = y+j
            if dx <0 or dy < 0 or dx >4 or dy > 5:continue
            if used[dx][dy] ==1 or arr[dx][dy]==1: continue
            used[dx][dy] =1
            q.append((dx,dy,cnt +1))




ans = 0
ans += bfs(0,0,4,0)
ans += bfs(4,0,4,5)
print(ans)


# 바다 섬

arr= [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
]

# 섬의 상태를 입력 받았을 때 섬의 크기 구하기
directions = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x,y):

    q= deque()
    size = 1
    q.append((x,y))
    arr[x][y]  =0
    while q:
        nx,ny = q.popleft()
        for i,j in directions:
            dx = nx+i
            dy = ny+j
            if dx <0 or dy < 0 or dx >4 or dy > 4:continue
            if arr[dx][dy] ==1 :    # 1 섬이라면
                size += 1
                q.append((dx,dy))
                arr[dx][dy]  =0     # used 따로 운영안하고 그냥 값을 바꿔버림
    return size

for  i in range(5):
    for  j in range(5):
        if arr[i][j] == 1: print(bfs(i,j))

# 응용 문제 풀어보기
print("practice")
arr=[
    [0,0,0,0,0,0],
    [0,1,0,0,1,0],
    [1,1,1,0,0,0],
    [0,1,0,0,1,1],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
]
directions = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x,y):
    q=deque()
    arr[x][y] = 0
    size = 1
    q.append((x,y))
    while q :
        nx,ny =q.popleft()
        for i,j in directions:
            dx = nx+i
            dy = ny+j
            if 0<=dx <6 and 0 <= dy <6:
                if arr[dx][dy] == 1:
                    size +=1
                    arr[dx][dy] =0
                    q.append((dx,dy))
    return size
cnt = 0
Max,Min = 0,10000
for i in range(6):
    for j in range(6):
        if arr[i][j] == 1:
            cnt +=1
            data = bfs(i,j)
            if data > Max : Max = data
            if data < Min : Min = data
            continue
print(cnt)
print(Max, Min, Max-Min)






