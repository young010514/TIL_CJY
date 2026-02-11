n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

directions = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
]


used = [[0] * n for _ in range(n)]
# print(used)
result = 0
def dfs(*point):
    global result
    x,y = point
    if x == n-1 and y == n-1 :
        result = 1
        return
    for dx, dy in directions:
        if 0 <= x + dx < n and 0 <= y + dy < n:
            if lst[x+dx][y+dy] == 0 and used[x+dx][y+dy] == 0:
                used[x + dx][y + dy] = 1
                dfs(x+dx, y+dy)
                used[x + dx][y + dy] = 0
dfs(0,0)
if result : print("가능")
else : print("불가능")


