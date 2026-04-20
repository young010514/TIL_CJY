from collections import deque

n,m = map(int,input().split())
arr= [input().split() for _ in range(n)]
# 우선 치즈로
# 다음엔 도시한테로 가야하는데,
# 이걸 for _ in range(2)로 구현해보기

directions = [(1,0),(-1,0),(0,1),(0,-1)]
s,d,c = 0,0,0

for i in range(n):
    if "S" in arr[i]: s = (i, arr[i].index("S"))
    if "C" in arr[i]: c = (i, arr[i].index("C"))
    if "D" in arr[i]: d = (i, arr[i].index("D"))
    if s and d and c : break
Sum = 0
# 우선 도착 치즈
stx, sty = s
edx, edy = c
for _ in range(2):
    used = [[0] * m for _ in range(n)]
    used[stx][sty] = 1
    q = deque()
    q.append([stx,sty,0])
    while q:
        nowx,nowy,cnt = q.popleft()
        if nowx == edx and nowy == edy :
            q.clear()
            break

        for i,j in directions:
            dx = nowx + i
            dy = nowy + j
            if dx <0 or dy <0 or dx >= n or dy >= m: continue
            if arr[dx][dy] == "x" : continue
            used[dx][dy] = 1
            q.append([dx,dy, cnt + 1])

    stx,sty = c
    edx, edy = d
    Sum += cnt
print(Sum)